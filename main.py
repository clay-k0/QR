"""
Author: Clayton King
Date: Fri 21 Apr 2023 07:11:29
Description: Generates and saves QR codes.
"""

import argparse
import os
from time import sleep

import qrcode
from alive_progress import alive_bar

def parse_args():
    """Parses command-line arguments and returns the QR code text, directory, and file name."""

    parser = argparse.ArgumentParser(description="Generate and save QR codes.")
    parser.add_argument("text", type=str, help="Text or URL for QR code")
    parser.add_argument("directory", type=str,
                        help="Directory to save QR code")
    parser.add_argument("file_name", type=str, help="Name of the QR code file")
    args = parser.parse_args()
    return args.text, args.directory, args.file_name


def get_user_choice(message, valid_choices):
    """Asks the user for input and returns it if it's a valid choice."""

    user_choice = input(message)
    while user_choice.lower() not in valid_choices:
        print("\nPlease enter a valid choice.")
        user_choice = input(message)
    return user_choice


def make_directory(directory):
    """Creates a directory if it doesn't exist."""

    if not os.path.exists(directory):
        print(f"\nCould not find the directory {directory}")

        choice = get_user_choice(
            "Would you like to create it? (y/n) ", ['y', 'Y', 'n', 'N'])

        if choice in {"y", "Y"}:
            print("\nAttempting to create directory...")
            try:
                os.makedirs(directory)
                sleep(1)
                print(f"Created {directory}")
            except OSError:
                print(f"Failed to create {directory}")
                exit(1)
        elif choice in {"n", "N"}:
            print("\nYou chose not to create the directory. Exiting...")
            exit(1)

    else:
        print(f"\nFound directory {directory}")


def overwrite_file(qr_code, directory, file_name):
    """Asks the user if they want to overwrite an existing file and saves the QR code if they do."""

    file_path = os.path.join(directory, file_name)

    if os.path.exists(file_path):
        print(f"\n{file_path} already exists.")
        overwrite = get_user_choice(
            "Would you like to overwrite the file? (y/n) ", ['y', 'Y', 'n', 'N'])
        if overwrite in {"y", "Y"}:
            try:
                save_file(qr_code, directory, file_name)
                exit(0)
            except OSError:
                print("\nQR code failed to save. Please try again.")
                exit(1)
        elif overwrite in {"n", "N"}:
            print("\nYou chose not to overwrite the file. Exiting...")
            exit(1)


def save_file(qr_code, directory, file_name):
    """Saves the QR code and displays a progress bar."""

    file_path = os.path.join(directory, file_name)

    if os.path.exists(directory):
        print("\nSaving file...")
        try:
            qr_code.save(file_path)
        except OSError:
                print("\nQR code failed to save. Please try again.")
                exit(1)
        with alive_bar(total=100, bar='classic2', spinner='classic') as bar:
            bar(1, skipped=True)
            for _ in range(1, 100):
                bar(1)
        print(f"\nQR code saved to: {file_path}")

    else:
        print("\nQR code failed to save. Please try again.")


def main():
    """Generates and saves a QR code based on command-line arguments."""

    # Parse command-line argument, get the QR code text, directory, and file name
    qr_text, directory, file_name = parse_args()

    # if the user enters a directory without a trailing slash, add it
    if directory[-1] != "/":
        directory += "/"

    # clean the file name
    file_name = file_name.split(".")[0]

    # Check if the directory exists
    make_directory(directory)

    # Ask user for file format choice
    file_format_choice = get_user_choice(
        "\nWould you like to save the QR image as a (1) .png or (2) .jpg? ", ['1', '2'])
    if file_format_choice == "1":
        file_name += ".png"
    elif file_format_choice == "2":
        file_name += ".jpg"

    # Check if the file already exists at the directory
    overwrite_file(qrcode.make(qr_text), directory, file_name)

    # Save the QR code
    save_file(qrcode.make(qr_text), directory, file_name)


if __name__ == "__main__":
    main()
