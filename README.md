# entry.B00M
#
#
## _Muddying The Phisher's Net_
#
entry.B00M is designed to provide an anonymous, easy-to-use tool for impeding scammers' phishing attempts through POST requests en-masse; the primary goal of the project is to:
* Populate the scammer's Google Form with large amounts of false data so real responses from victims are not apparent 
* Inindate scammers' Google Forms with enough data that they are unwilling to trudge through it to look for genuine responses
#
## Features
- Use a '-v' when running the program to turn on verbose mode
    - View an example of the data being sent
- The POST requests being sent are outputted to the terminal with additional data:
    - The generated user agent being used for the request
    - The proxy IP Address being used for the requests
    - The status code which the request returned

## Mechanics
- Google Forms utilize an "entry.id=########" to specify the answers that correlate to the corresponding questions; entry.B00M uses this concept to pass randomly generated values to the scammer's form.

#
#
The Latest 2024 Phishing Statistics [AAG IT](https://aag-it.com/the-latest-phishing-statistics/)
> Phishing is the most common form of cyber crime, 
> with an estimated 3.4 billion spam emails sent every day...
> the top 5 most imitated brands in Q1 2022 were:
> 1. LinkedIn (52%)
> 2. DHL (14%)
> 3. Google (7%)
> 4. Microsoft (6%)
> 5. FedEx (6%)

## Tech

entry.B00M uses a number of packages to work properly:

- [termcolor] - ANSI color formatting for output in terminal 
- [pyfiglet] - Pure-python FIGlet implementation
- [random-user-agent] - A package to get random user agents based filters provided by user
- [requests] - Python HTTP for Humans
- [urllib3] - HTTP library with thread-safe connection pooling, file post, and more
- [tabulate] - Pretty-print tabular data
- [selenium] - The selenium package is used to automate web browser interaction from Python.
- [bs4] - Screen-scraping library
- [names] - Generate random names

entry.B00M itself is open source with a [public repository](https://github.com/DannyGaev/entryBoom) on GitHub.

## Installation

Install the dependencies and devDependencies and start the server.

```sh
cd entryBoom
pip3 install -r requirements.txt
python3 entryBoom.py
```

## License

MIT

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [termcolor]: <https://pypi.org/project/termcolor/>
   [pyfiglet]: <https://pypi.org/project/pyfiglet/>
   [random-user-agent]: <https://pypi.org/project/random-user-agent/>
   [requests]: <https://pypi.org/project/requests/>
   [urllib3]: <https://pypi.org/project/urllib3/>
   [tabulate]: <https://pypi.org/project/tabulate/>
   [selenium]: <https://pypi.org/project/selenium/>
   [bs4]: <https://pypi.org/project/beautifulsoup4/>
   [names]: <https://pypi.org/project/names/>
