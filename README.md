# QReate

A simple Python script that generates and saves QR codes. The user can choose the text, directory, and file name. They can also choose the file format (PNG or JPG).

## Getting Started

## **Prerequisites**

To run the script, you will need to have Python 3 installed.

You will also need to install the following packages:

- qrcode
- alive-progress

To install the packages, run the following commmand:

`pip install -r requirements.txt`

or

`pip3 install -r requirements.txt`

## **Installing**

Clone or download the repository.\
Open the terminal or command prompt and navigate to the project directory.\
Run the script using the following command:

**"python3 main.py <text/url> <directory> <file_name>"**

`<text/url>`: The text or URL for the QR code.\
`<directory>`: The directory to save the QR code.\
`<file_name>`: The name of the QR code file.

For example:

`python3 main.py https://google.com /path/to/directory/ example`

## **Usage**

1. Run the script using the command above.

2. If the file already exists, choose whether to overwrite it.

3. If the directory does not exist, choose whether to create it.

4. Choose the file format (PNG or JPG).

5. The QR code will be generated and saved to the specified directory.

## Authors

Clayton King

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
