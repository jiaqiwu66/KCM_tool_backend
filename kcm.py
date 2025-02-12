from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
cors = CORS(app, origins="*")
@app.route('/upload', methods=['POST'])
def upload_file():

    if 'operational' not in request.files or 'base' not in request.files:
        data = {'message': 'Missing files', 'status': 'error'}
        return jsonify(data), 400

    operational = request.files['operational']
    base = request.files['base']
    print(operational)
    print(base)

    # # read CSV file
    df = pd.read_csv(operational)
    def categorize_split(row):
        if row['Vehicle Size'] == 40:
            result = (row['Distance\n(mi)'] * 2.08) / (525 * 0.7)
        elif row['Vehicle Size'] == 60:
            result = (row['Distance\n(mi)'] * 2.9) / (525 * 0.7)
        else:
            return "Unknown"  # Others mark as Unknown

        # sort based on results
        if result < 1:

            return "no split needed"
        elif 1 <= result < 2:
            return "one split"
        else:
            return "two split or more"

    df['split category'] = df.apply(categorize_split, axis=1)
    count = df['split category'].value_counts()
    print(count)

    no_split = (df['split category'] == 'no split needed').sum()
    one_split = (df['split category'] == 'one split').sum()
    two_split = (df['split category'] == 'two split or more').sum()
    # save as new CSV file
    output_file = "processed_file.csv"
    df.to_csv(output_file, index=False)

    print(f"Save the result to {output_file}")

    data = {
        'message': 'Data fetched successfully!',
        'data': {
            'no_split': str(no_split),
            'one_split': str(one_split),
            'two_split': str(two_split),
        }
    }
    # return the statistics result
    # return jsonify(data), 200
    file_path = os.path.join(app.root_path, 'processed_file.csv')
    return send_file(file_path, as_attachment=True, download_name="result.csv")

if __name__ == '__main__':
    app.run(port=5050, debug=True)

