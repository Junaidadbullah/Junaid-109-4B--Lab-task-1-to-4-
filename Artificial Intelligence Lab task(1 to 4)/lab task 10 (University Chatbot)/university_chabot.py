import nltk
from nltk.chat.util import Chat



pairs = [
    (r"(?i).*superior university known for.*", 
     ["Superior University is known for its academic excellence, innovative teaching methods, and entrepreneurship-focused education."]),
    (r"(?i).*admissions open.*", 
     ["Admissions usually open before the start of the Fall and Spring semesters. Check our website for current dates."]),
    (r"(?i).*apply online.*", 
     ["Yes, you can apply online through the official Superior University admission portal."]),
    (r"(?i).*contact.*admission.*", 
     ["You can contact the admissions office via phone, email, or by visiting the main campus."]),
    (r"(?i).*documents required.*admission.*", 
     ["Required documents include academic transcripts, CNIC/Form-B, passport-size photographs, and any entry test results."]),
    (r"(?i).*evening programs.*", 
     ["Yes, Superior University offers evening and weekend programs for working professionals."]),
    (r"(?i).*recognized by HEC.*", 
     ["Yes, Superior University is recognized by the Higher Education Commission (HEC) of Pakistan."]),
    (r"(?i).*medium of instruction.*", 
     ["The medium of instruction is English for most programs."]),
    (r"(?i).*sports.*activities.*", 
     ["Yes, we offer a wide range of clubs, societies, and sports for student development."]),
    (r"(?i).*transfer credits.*", 
     ["Yes, credit transfers are allowed after evaluation of your transcript by the academic committee."]),
    (r"(?i).*age limit.*admission.*", 
     ["No strict age limit exists, but eligibility criteria must be met."]),
    (r"(?i).*facilities available.*campus.*", 
     ["Our campus includes libraries, labs, sports facilities, cafeterias, and student lounges."]),
    (r"(?i).*job placement.*", 
     ["Yes, our career services department assists students with internships and job placements."]),
    (r"(?i).*part-time programs.*", 
     ["Yes, part-time and weekend options are available for some programs."]),
    (r"(?i).*apply for more than one program.*", 
     ["Yes, you can apply for multiple programs but must meet the criteria for each."]),
    (r"(?i).*miss.*admission deadline.*", 
     ["Late applications may be considered based on seat availability and department approval."]),
    (r"(?i).*admission process take.*", 
     ["The process usually takes 1–2 weeks after submission of complete documents."]),
    (r"(?i).*laptops required.*", 
     ["While not mandatory for all, laptops are highly recommended, especially for IT-related programs."]),
    (r"(?i).*admission tests.*online.*", 
     ["Some entry tests may be conducted online, depending on the department’s policy."]),
    (r"(?i).*check.*admission status.*", 
     ["After applying, you can check your status through the online admission portal or contact admissions."]),
    (r".*", ["I'm sorry, I don't have information about that. Could you rephrase?"])
]

chatbot = Chat(pairs)


def chatbot_app(user_input):
    if user_input.lower() in ["quit", "bye"]:
        return "Goodbye! Have a great day 😊"
    response = chatbot.respond(user_input)
    return response


        

