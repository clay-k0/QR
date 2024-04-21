"""
Author: Clayton King
Date: Sun 21 Apr 2024
Description: Generates and saves QR codes.
"""

import argparse
import os
import qrcode
from alive_progress import alive_bar


def parse_args():
    """ Parses command-line arguments. """
    parser = argparse.ArgumentParser(description="Generate and save QR codes.")
    parser.add_argument("text", type=str, help="Text or URL for QR code")
    parser.add_argument("directory", type=str,
                        help="Directory to save QR code")
    parser.add_argument("file_name", type=str, help="Name of the QR code file")
    return parser.parse_args()


def make_directory(directory):
    """ Creates a directory if it doesn't exist. """
    if not os.path.exists(directory):
        print(f"\nAttempting to create directory: {directory}")
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"Directory created: {directory}")
        except OSError as e:
            print(f"Failed to create {directory}: {e}")
            return False
    return True


def save_file(qr_code, file_path):
    """ Saves the QR code file. """
    print("\nSaving file...")
    try:
        qr_code.save(file_path)
        with alive_bar(total=100, bar='classic2', spinner='classic') as bar:
            for i in range(100):
                bar()
        print(f"\nQR code saved to: {file_path}")
    except OSError as e:
        print(f"\nFailed to save QR code: {e}")


def get_file_format_choice():
    """ Asks the user for their preferred file format. """
    choice = input(
        "\nWould you like to save the QR image as a (1) .png or (2) .jpg? ")
    while choice not in {'1', '2'}:
        print("Please enter a valid choice: 1 for .png or 2 for .jpg")
        choice = input(
            "\nWould you like to save the QR image as a (1) .png or (2) .jpg? ")
    return '.png' if choice == '1' else '.jpg'


def main():
    """ Main function to handle the logic. """
    args = parse_args()
    directory = os.path.abspath(args.directory)
    file_format = get_file_format_choice()
    file_name = f"{os.path.splitext(args.file_name)[0]}{file_format}"

    if make_directory(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.exists(file_path):
            if input(f"{file_path} already exists. Overwrite? (y/n) ").lower() != 'y':
                print("Operation cancelled.")
                return
        qr_code = qrcode.make(args.text)
        save_file(qr_code, file_path)


if __name__ == "__main__":
    main()
