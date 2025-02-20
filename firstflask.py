from flask import Flask, render_template, request, render_template_string
import random
import json, jsonify


app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello, World!"

@app.route("/stat")
def helloSTAT():
    return "Hello, STAT KUU!"

@app.route("/statHTML") 
def helloSTAThtml():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stat KKU - Homepage</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            header {
                background-color: #0078d7;
                color: white;
                padding: 1rem 0;
                text-align: center;
            }
            nav {
                background-color: #005ea6;
                display: flex;
                justify-content: center;
                padding: 0.5rem 0;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 1rem;
            }
            nav a:hover {
                text-decoration: underline;
            }
            main {
                padding: 2rem;
                text-align: center;
            }
            footer {
                background-color: #0078d7;
                color: white;
                text-align: center;
                padding: 1rem 0;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Stat KKU</h1>
            <p>Department of Statistics, Khon Kaen University</p>
        </header>
        <nav>
            <a href="#about">About Us</a>
            <a href="#programs">Programs</a>
            <a href="/research">Research</a>
            <a href="/contact">Contact</a>
        </nav>
        <main>
            <section id="about">
                <h2>About Us</h2>
                <p>The Department of Statistics at Khon Kaen University is a leading institution dedicated to advancing the field of statistics through education, research, and community engagement.</p>
                <p>Established with a vision to excel in statistical sciences, the department has consistently maintained high standards in academic and research pursuits.</p>
                <p>Our mission is to provide students with a solid foundation in statistical theory and methods, equipping them to solve real-world problems effectively.</p>
                <p>We offer a dynamic learning environment that combines theoretical knowledge with practical applications, ensuring our graduates are well-prepared for various career paths.</p>
                <p>The department's faculty members are highly experienced and bring a wealth of knowledge from diverse areas of statistics, mathematics, and data science.</p>
                <p>Over the years, we have established strong collaborations with industry and government agencies, contributing to meaningful projects and innovations.</p>
                <p>Our students have the opportunity to participate in research initiatives that address pressing challenges in healthcare, business, environment, and technology.</p>
                <p>We are committed to fostering a culture of curiosity and critical thinking, encouraging students to explore new horizons in statistical applications.</p>
                <p>Our alumni network spans across the globe, with graduates holding prestigious positions in academia, industry, and government sectors.</p>
                <p>At the Department of Statistics, we believe in making a positive impact on society through statistical knowledge and innovation.</p>
            </section>
            <section id="programs">
                <h2>Programs</h2>
                <p>We offer undergraduate and postgraduate programs in statistics to prepare students for successful careers.</p>
            </section>
            <section id="research">
                <h2>Research</h2>
                <p>Our faculty members are engaged in cutting-edge research to address real-world challenges using statistical methods.</p>
            </section>
            <section id="contact">
                <h2>Contact</h2>
                <p>Email: info@statkku.ac.th</p>
                <p>Phone: +66-1234-5678</p>
            </section>
        </main>
        <footer>
            <p>&copy; 2025 Stat KKU. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """
@app.route("/research")
def research_page():
    faculty_research = {
    "Dr. Alice Smith": [
        "สภาพอากาศ Statistical Modeling of Climate Change Impacts",
        "อนุกรมเวลา Advanced Methods in Time Series Analysis",
        "การเรียนรู้ของเครื่อง Machine Learning Applications in Biostatistics",
    ],
    "Dr. Bob Johnson": [
        "Bayesian Inference in Social Sciences",
        "Quantitative Analysis of Economic Trends",
        "Development of Robust Statistical Software",
    ],
    "Dr. Carol Davis": [
        "Optimization Techniques in Big Data Analytics",
        "Statistical Approaches to Epidemiology",
        "Survey Data Analysis for Policy Decisions",
    ],
    }

    faculty_py, research_projects_py = random.choice(list(faculty_research.items()))
    
    return render_template("research.html", faculty=faculty_py, research_projects=research_projects_py)

@app.route("/contact",methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        user_email = request.form.get("email")
        return render_template_string("""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Contact Us</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            margin: 0;
                            padding: 0;
                            background-color: #f9f9f9;
                            color: #333;
                        }
                        header {
                            background-color: #0078d7;
                            color: white;
                            text-align: center;
                            padding: 1rem 0;
                        }
                        main {
                            padding: 2rem;
                            max-width: 600px;
                            margin: auto;
                            text-align: left;
                            background: white;
                            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                            border-radius: 8px;
                        }
                        h1 {
                            color: #005ea6;
                        }
                        p {
                            line-height: 1.6;
                        }
                        footer {
                            text-align: center;
                            margin-top: 2rem;
                            font-size: 0.9rem;
                            color: #666;
                        }
                        .home-button {
                            display: inline-block;
                            margin-bottom: 1rem;
                            padding: 0.5rem 1rem;
                            background-color: #005ea6;
                            color: white;
                            text-decoration: none;
                            border-radius: 5px;
                            font-size: 1rem;
                        }
                        .home-button:hover {
                            background-color: #003d73;
                        }
                    </style>
                </head>
                <body>
                    <header>
                        <h1>Contact Us</h1>
                    </header>
                    <main>
                        <a href="/statHTML" class="home-button">Home</a>
                        <a href="/contact" class="home-button">Contact</a>

                        <h2><a>Admin<a> Contact Details</h2>
                        <p><strong>Name:</strong> Ratchanont Thippimanporn</p>
                        <p><strong>Email:</strong> admin@example.com</p>
                        <p><strong>Phone:</strong> +1-234-567-890</p>
                        <p>If you have any questions or need assistance, please don’t hesitate to reach out. Our admin is here to help you!</p>
                        <h2>Thank you {{user}}</h2>
                    </main>
                    <footer>
                        <p>&copy; 2025 Stat KKU. All rights reserved.</p>
                    </footer>
                </body>
                </html>
                """,user=user_email)

    else:
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contact - Stat KKU</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f9;
                    color: #333;
                }
                header {
                    background-color: #0078d7;
                    color: white;
                    padding: 1rem 0;
                    text-align: center;
                }
                main {
                    padding: 1rem;
                    max-width: 800px;
                    max-height: auto;
                    margin: 0 auto;
                    background: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }
                main h1 {
                    margin-bottom: 1rem;
                }
                .contact-details {
                    text-align: left;
                }
                .contact-details h2 {
                    margin-top: 1.5rem;
                    color: #005ea6;
                }
                footer {
                    background-color: #0078d7;
                    color: white;
                    text-align: center;
                    padding: 1rem 0;
                    position: fixed;
                    bottom: 0;
                    width: 100%;
                }
                .home-button {
                    display: inline-block;
                    margin-bottom: 1rem;
                    padding: 0.5rem 1rem;
                    background-color: #005ea6;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-size: 1rem;
                }
                .home-button:hover {
                    background-color: #003d73;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Contact Us - Stat KKU</h1>
                <p>Get in touch with the Department of Statistics, Khon Kaen University</p>
            </header>
            <main>
                <a href="/statHTML" class="home-button">Home</a>
                
                <h1>Contact Information</h1>
                <div class="contact-details">
                    <h2>General Inquiries</h2>
                    <p>Email: info@statkku.ac.th</p>
                    <p>Phone: +66-1234-5678</p>

                    <h2>Administrative Contact</h2>
                    <p>Name: Dr. Ratchanont Thippimanporn</p>
                    <p>Role: Department Administrator</p>
                    <p>Email: admin@statkku.ac.th</p>
                    <p>Phone: +66-9876-5432</p>
                            
                    <p>If you have any questions or need assistance, please don’t hesitate to reach out. Our admin is here to help you!</p>
                    <h2>Submit Your Email So We Can Contact You Back</h2>
                    <form method="POST">
                        <label for="email">Your Email:</label>
                        <input type="email" id="email" name="email" required placeholder="Enter your email">
                        <button type="submit">Submit</button>
                    </form>
                </div>
            </main>

            <footer>
                <p>&copy; 2025 Stat KKU. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """

##api

# @app.route('/simpleAPI',methods=['POST'])
# def web_service_API():

#     payload = request.data.decode("utf-8")
#     inmessage = json.loads(payload)

#     print(inmessage)
    
#     json_data = json.dumps({'y': 'received!'})
#     return json_data

@app.route('/simpleAPI', methods=['POST'])
def simpleAPI():
    try:
        # รับข้อมูลจาก request
        payload = request.data.decode("utf-8")
        inmessage = json.loads(payload)

        # แสดงข้อมูลที่ได้รับใน log
        print("\n[INFO] ข้อมูลที่ได้รับจากผู้ใช้:")
        print(f"----------------------------")
        print(f"ข้อความที่ได้รับ: {inmessage.get('msg')}")
        print(f"ผู้ส่ง: {inmessage.get('ผู้ส่ง')}")
        print(f"ผู้รับ: {inmessage.get('ผู้รับ')}")
        print(f"IP ของผู้รับ: {inmessage.get('ip')}")
        print(f"----------------------------\n")

        # สร้างข้อมูลที่ต้องการส่งกลับ
        json_data = json.dumps({'y': 'received!'})

        # ส่งข้อมูลกลับไป
        return json_data, 200  # คืนค่า HTTP Status 200 เพื่อบอกว่า request สำเร็จ

    except Exception as e:
        # ในกรณีเกิดข้อผิดพลาด
        error_message = f"[ERROR] ข้อผิดพลาด: {str(e)}"
        print(error_message)

        # ส่งข้อผิดพลาดกลับไป
        return jsonify({'error': 'เกิดข้อผิดพลาดในการประมวลผลข้อมูล'}), 400

if __name__ == "__main__":  # run code
    app.run(host='0.0.0.0',debug=True,port=5006)
