# search-github
##### Version 1
CLI application which takes in a search term and searches GitHub repositories for that term and outputs the results in CSV format.


### Machine Problem: GitHub API
You need to create a CLI application which takes in a search term and searches GitHub repositories for that term. It should output the results in CSV format.

#### Requirements:

* The application takes in a search term as the command line argument
* It should output a CSV file containing the name of the project, the description, the URL of the repository, the programming language used and the date where it was last updated
* The application should output up to up to 1000 search results if possible
* Output should be the format: output-yyy-mm-dd-hh-m.csv
* Implement Basic or OAuth2 authentication. Remember not to commit your credentials!

## Usage

```
python main.py -u <username> <word_to-search>
```

## Built With
* [Python](https://www.python.org/downloads/) v3.7
* [Jetbrains PyCharm Community Edition 2019](https://www.jetbrains.com/pycharm/download/) - IDE

## Authors

* **Damaris Gregorio** - *Initial work* - [Dam Gregorio](https://github.com/damiiegregorio)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
