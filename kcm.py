from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
cors = CORS(app, origins="*")

split_result = {}
@app.route('/upload', methods=['POST'])
def upload_file():

    if 'operational' not in request.files or 'base' not in request.files:
        data = {'message': 'Missing files', 'status': 'error'}
        return jsonify(data), 400

    operational = request.files['operational']
    base = request.files['base']
    print(operational)
    print(base)

    # # 读取CSV文件
    df = pd.read_csv(operational)
    def categorize_split(row):
        if row['Vehicle Size'] == 40:
            result = (row['Distance\n(mi)'] * 2.08) / 525
        elif row['Vehicle Size'] == 60:
            result = (row['Distance\n(mi)'] * 2.9) / 525
        else:
            return "Unknown"  # Others mark as Unknown

        # 根据计算结果进行分类
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
    # 保存新的CSV文件
    output_file = "processed_file.csv"
    df.to_csv(output_file, index=False)

    print(f"Save the result to {output_file}")

    split_result['one_split'] = int(one_split)
    split_result['two_split'] = int(two_split)
    split_result['no_split'] = int(no_split)
    split_result['total'] = int(no_split + one_split + two_split)

    # return the statistics result
    # return jsonify(data), 200

    file_path = os.path.abspath('/home/jwu66/processed_file.csv')
    return send_file(file_path, as_attachment=True, download_name="result.csv", cache_timeout=0)


@app.route("/getResult", methods=["GET"])
def get_result():

    if not split_result:
        return jsonify({'message': 'No data available'}), 400
    return jsonify(split_result)





    # file_path = os.path.abspath('/home/jwu66/processed_file.csv')
    # return send_file(file_path, as_attachment=True, download_name="result.csv", cache_timeout=0)

    # file_path = "processed_file.csv"

    # with open(file_path, "rb") as f:
    #     data = f.read()

    # return Response(
    #     data,
    #     mimetype="text/csv",
    #     headers={"Content-Disposition": "attachment; filename=result.csv"}
    # )

