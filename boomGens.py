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


def genPayload(entryIds, categories, answers, session, user_agent):
    payload = {}
    x = 0
    for category in categories:
        rand = random.randint(1, 2) == 1
        c = category.lower()
        el = ""
        if "date of birth" in c or "d.o.b" in c or "date" in c:
            payload["entry."+entryIds[x][0]] = answers[x][1][0]
            payload["entry."+entryIds[x][1]] = answers[x][1][1]
            payload["entry."+entryIds[x][2]] = answers[x][1][2]
        elif (answers[x][0] > 0):
            rand2 = random.randint(0, len(answers[x][1])-1)
            willBe = answers[x][1][rand2]
            try:
                willBe = willBe.replace("\\", "").replace('"', '')
            except:
                continue
            el = willBe
            payload["entry."+entryIds[x]] = el
        else:
            if "name" in c:
                el = genNames(1)[0]
            elif "local" in c or "mailing" in c or "address" in c or "state" in c or "city" in c:
                el = genInput(7)
            elif "zip" in c:
                el = genInput(5)
            elif "phone" in c:
                el = genNumber()
            elif "id" in c:
                el = genInput(5)
            elif "gender" in c:
                el = "Female" if rand else "male"
            elif "do you" in c or "are you" in c or "i know how to" in c or "how to" in c:
                el = "Yes" if rand else "No"
            elif "age" in c:
                el = "21"
            elif "occupation" in c or "job" in c or "position" in c:
                el = ''.join(genJob())
            elif "pass" in c or "password" in c or "key word" in c or "keyword" in c:
                el = genInput(15)
            elif "email address" in c:
                found = False
                while not found:
                    response = session.get(
                        "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1", headers={'User-Agent': user_agent})
                    try:
                        el = json.loads(response.text)[0]
                        found = True
                    except:
                        pass
            elif "School Attended" in c or "school attended" in c:
                el = genNames(1)[0]
            elif "year" in c:
                el = genInput(4)
            elif "time" in c:
                rand2 = random.randint(1, 3)
                match rand2:
                    case 1:
                        el = "Morning"
                    case 2:
                        el = "Afternoon"
                    case 3:
                        el = "Evening"
            elif "e-mail" in c or "email" in c or "mail" in c:
                found = False
                while not found:
                    response = session.get(
                        "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1", headers={'User-Agent': user_agent})
                    try:
                        el = json.loads(response.text)[0]
                        found = True
                    except:
                        pass
            elif "comments" in c:
                rand2 = random.randint(1, 5)
                match rand2:
                    case 1:
                        el = "We have collected information about your computer and network -- it will be reported to the proper authorities. Good luck."
                    case 2:
                        el = "How do I use the service?"
                    case 3:
                        el = "I had a few questions abut the pay ! Contact me at my other email at  supposedChi1ck3n@proton.me, thank yuo!"
                    case 4:
                        el = "As a {job}, how would I go about quitting and transferring to you? thanks!".format(
                            job=''.join(genJob()))
                    case 5:
                        el = "."
            payload["entry."+entryIds[x]] = el
        x += 1
    return payload
