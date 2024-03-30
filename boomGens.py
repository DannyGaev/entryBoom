import random
import string
import names
import json


def genNumber():
    numbers = ["13258336805", "16028391470", "16234038423", "15598821587", "14079539001", "18172490670", "13139736661", "13415881208", "13853672933", "13517631532",
               "13079317251", "18394269809", "13806668844", "15058651516", "18593126027", "17862698095", "18655340204", "14058856815", "17139672266", "12544248766"]
    return numbers[random.randint(0, len(numbers)-1)]


def genInput(rangeOf):
    return ''.join(random.choice(string.ascii_uppercase + string.digits)
                   for _ in range(rangeOf))


def genJob():
    dict = {
        "verbs": [
            "Lead",
            "Senior",
            "Direct",
            "Corporate",
            "Dynamic",
            "Future",
            "Product",
            "National",
            "Regional",
            "District",
            "Central",
            "Global",
            "Customer",
            "Investor",
            "Dynamic",
            "International",
            "Legacy",
            "Forward",
            "Internal",
            "Human",
            "Chief",
            "Principal",
            "Lead",
            "Senior",
            "Direct",
            "Corporate",
            "Dynamic",
            "Future",
            "Product",
            "National",
            "Regional",
            "District",
            "Central",
            "Global",
            "Customer,",
            "Investor",
            "Dynamic",
            "International",
            "Legacy",
            "Forward",
            "Internal",
            "Human",
            "Chief",
            "Principal",
        ],
        "adjectives": [
            "Solutions",
            "Program",
            "Brand",
            "Security",
            "Research",
            "Marketing",
            "Directives",
            "Implementation",
            "Integration",
            "Functionality",
            "Response",
            "Paradigm",
            "Tactics",
            "Markets",
            "Group",
            "Division",
            "Applications",
            "Optimization",
            "Operations",
            "Communications",
            "Web",
            "Quality",
            "Assurance",
            "Accounts",
            "Creative",
            "Accountability",
            "Interactions",
            "Factors",
            "Usability",
            "Metrics",
        ],
        "nouns": [
            "Supervisor",
            "Associate",
            "Executive",
            "Liason",
            "Officer",
            "Manager",
            "Engineer",
            "Specialist",
            "Director",
            "Coordinator",
            "Administrator",
            "Architect",
            "Analyst",
            "Designer",
            "Planner",
            "Orchestrator",
            "Technician",
            "Developer",
            "Producer",
            "Consultant",
            "Assistant",
            "Facilitator",
            "Agent",
            "Representative",
            "Strategist",
            "Supervisor",
            "Associate",
            "Executive",
            "Liason",
            "Officer",
            "Manager",
            "Engineer",
            "Specialist",
            "Director",
            "Coordinator",
            "Engineer",
            "Specialist",
            "Director",
            "Vice President",
            "Officer",
            "VP",
        ]
    }
    verbsLen = len(dict["verbs"])
    adjLen = len(dict["adjectives"])
    nounLen = len(dict["nouns"])

    vI = random.randint(0, verbsLen-1)
    aI = random.randint(0, adjLen-1)
    nI = random.randint(0, nounLen-1)

    return ({"{verb} {adjective} {noun}".format(verb=dict["verbs"][vI], adjective=dict["adjectives"][aI], noun=dict["nouns"][nI])})


def genNames(count):
    allNames = [names.get_full_name() for x in range(count)]
    return allNames


def genPayload(entryIds, categories, session, user_agent):
    payload = {}
    for x in range(0, len(categories)):
        rand = random.randint(1, 2) == 1
        c = categories[x].lower()
        el = ""
        if "name" in c:
            el = genNames(1)[0]
        elif "local" in c or "mailing" in c or "address" in c or "state" in c or "city" in c:
            el = genInput(7)
        elif "zip" in c:
            el = genInput(5)
        elif "phone" in c:
            el = genNumber()
        elif "gender" in c:
            el = "Female" if rand else "Male"
        elif "do you" in c or "are you" in c:
            el = "YES" if rand else "NO"
        elif "age" in c:
            el = "21"
        elif "occupation" in c or "job" in c or "position" in c:
            el = ''.join(genJob())
        elif "e-mail" in c or "email" in c:
            found = False
            while not found:
                response = session.get(
                    "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1", headers={'User-Agent': user_agent})
                try:
                    el = json.loads(response.text)[0]
                    found = True
                except:
                    pass
        payload["entry."+entryIds[x]] = el
    return payload
