from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask Scoring API ishlayapti!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # JSON ma'lumotni olish
        data = request.get_json()

        # features massivini olish
        features = data.get('features', [])
        if not features:
            return jsonify({"error": "features kiritilmagan!"}), 400

        # Oddiy hisoblash (namuna uchun)
        score = sum(features) / len(features)

        # Natijani qaytarish
        return jsonify({
            "status": "success",
            "input_features": features,
            "predicted_score": round(score, 2)
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
