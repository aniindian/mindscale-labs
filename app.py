from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Mindscale Labs</title>
        <link rel="icon" type="image/x-icon" href="/static/favicon1.png">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
        <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
        <style>
          @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
          body {
            font-family: 'Inter', sans-serif;
          }
        </style>
    </head>
    <body class="bg-black text-white">

        <!-- Navbar -->
        <nav class="flex justify-between items-center p-6 bg-black border-b border-gray-800">
            <div class="text-xl font-bold text-white"> Mindscale Labs</div>
            <div class="space-x-4">
                <a href="#" class="text-gray-300 hover:text-white">Products</a>
                <a href="#" class="text-gray-300 hover:text-white">Team</a>
                <a href="#" class="text-gray-300 hover:text-white">Join Waitlist</a>
            </div>
        </nav>

        <!-- Hero Section -->
        <section class="text-center py-20 px-6 bg-gradient-to-r from-black via-gray-900 to-gray-800">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">Scaling Intelligence for Bharat and Beyond</h1>
            <p class="text-lg md:text-xl max-w-2xl mx-auto text-gray-300">
                AI that speaks your language, understands your reality, and scales globally.
            </p>
            <div class="mt-6 flex justify-center gap-4">
                <a href="#" class="bg-blue-500 text-white px-6 py-2 rounded-full font-semibold hover:bg-blue-600">Join the Waitlist</a>
                <a href="#" class="border border-white px-6 py-2 rounded-full hover:bg-white hover:text-black">See How It Works</a>
            </div>
        </section>

        <!-- LangGround Flow with Animation -->
        <section class="py-20 px-6 text-center bg-gradient-to-b from-gray-900 to-black">
            <h2 class="text-3xl font-bold mb-4">LangGround AI Flow</h2>
            <p class="text-lg text-gray-300 max-w-3xl mx-auto mb-16">
                A complete pipeline to convert videos into regionally customized experiences using AI.
            </p>
            <div class="flex flex-wrap justify-center gap-6 max-w-5xl mx-auto">
                {% for step in steps %}
                <div data-aos="zoom-in" class="bg-gray-800 border border-gray-700 p-6 rounded-xl w-44 shadow-lg">
                    <h4 class="text-white font-bold text-md mb-2 flex items-center justify-center">
                        <span class="text-xl mr-2">{{ step.icon }}</span>{{ step.title }}
                    </h4>
                </div>
                {% endfor %}
            </div>
        </section>

        <!-- CTA Section -->
        <section class="py-20 px-6 text-center bg-gradient-to-r from-blue-700 to-indigo-800">
            <h2 class="text-3xl font-bold mb-4">Ready to Join the Journey?</h2>
            <a href="#" class="bg-white text-blue-700 px-8 py-3 rounded-full font-semibold hover:bg-gray-100">Join the Waitlist</a>
        </section>

        <!-- Footer -->
        <footer class="bg-gray-950 text-white py-10 text-center">
            <p>© 2025 Mindscale Labs — All rights reserved</p>
            <p class="text-sm mt-2">contact@mindscale.labs</p>
        </footer>

        <script>
          AOS.init({
            duration: 800,
            once: true,
          });
        </script>
    </body>
    </html>
    """, steps=[
        {"title": "User Shares Video Link", "icon": "🔗"},
        {"title": "Select Regional Language", "icon": "🌐"},
        {"title": "Transcribe with Whisper", "icon": "📝"},
        {"title": "Translate via NLLB", "icon": "🌍"},
        {"title": "Voiceover with Coqui/Bark", "icon": "🔊"},
    ])

if __name__ == "__main__":
    app.run(debug=True)


