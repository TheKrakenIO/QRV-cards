# QRV-card


## Introduction

The `rqr1.py` script is a Python tool that generates a customizable QR code encoding a vCard (version 3.0) with user-provided contact information. It allows users to create professional QR codes with styled dot patterns (rounded, circular, or square gradient) and output options (image, ASCII art, or both). The script is interactive, prompting users for contact details and QR code preferences, and includes robust error handling and input validation.

### Features

- **Customizable vCard**: Include contact details such as full name (required), last name, first name, organization, job title, phone number, email, and a note. Optional fields are excluded if left blank.
- **Required Field**: Full name is mandatory to ensure a valid vCard.
- **Optional Fields**: The following fields are included only if provided: last name, first name, organization, title, phone, email, and note. Invalid phone or email inputs are excluded.
- **Styled QR Codes**: Choose from three dot styles: `rounded`, `circle`, or `square_gradient`, with ASCII previews.
- **Output Options**: Save as a PNG image (`artistic_qr_code.png`), ASCII art (`artistic_qr_code.txt`), or both.
- **Image Enhancements**: QR code images have rounded corners and are resized to the user-specified size.
- **Error Handling**: Validates inputs (e.g., QR code size, phone, email) and handles file operation errors.
- **Dynamic QR Version**: Automatically adjusts QR code version to fit the vCard data.

---

## How to Use

### Prerequisites

- **Python 3.6+**
- **Libraries**:
  - `qrcode`
  - `Pillow`

### Installation

1. **Install Python** from [python.org](https://www.python.org/downloads/)
2. **Install dependencies**:
   ```bash
   pip install qrcode pillow
   ```

3. **Download the Script**: Save the `rqr1.py` script to your working directory.

---

### Running the Script

#### 1. Open a Terminal or Command Prompt  
Navigate to the directory containing `rqr1.py`.

#### 2. Execute the Script
```bash
python rqr1.py
```

#### 3. Follow the Prompts

---

### Contact Information

- **Full Name (required)**:  
  Enter a name (e.g., `John Doe`). You must provide a value, or the script will prompt again.

- **Optional Fields**:  
  Enter values for last name, first name, organization, job title, phone number (e.g., `+1234567890`), email (e.g., `john@example.com`), and note (e.g., `Meeting at 5 PM`).  
  Press Enter to skip any optional field, and it will be excluded from the vCard.

- **Validation**:  
  Phone numbers must start with `+` followed by digits.  
  Emails must contain `@`.  
  Invalid inputs are excluded.

---

### QR Code Customization

- **Size**:  
  Enter the QR code size in pixels (e.g., `400`).  
  Non-numeric or negative values default to `400`.

- **Output Type**:  
  Choose `image`, `ascii`, or `both`.  
  Invalid inputs default to `image`.

- **Dot Style**:  
  Select from `rounded`, `circle`, or `square_gradient` after viewing ASCII previews.  
  Invalid inputs default to `rounded`.

---

### Output

- If `image` or `both` is selected, a PNG file (`artistic_qr_code.png`) is saved with the styled QR code.
- If `ascii` or `both` is selected, ASCII art is printed to the console and saved as `artistic_qr_code.txt`.
- The QR code encodes the vCard, which QR code readers can scan to import contact details.

---

## Example Usage

```bash
$ python rqr1.py
Enter your contact information for the QR code (press Enter to exclude optional fields):
Full Name (required): John Doe
Last Name: Doe
First Name: John
Organization: 
Job Title: 
Phone Number (e.g., +1234567890): +1234567890
Email: john@example.com
Note: Meeting at 5 PM

Enter QR code size in pixels (e.g., 400): 400
Output type (image, ascii, or both): both

Choose a dot style for your QR code. Here are previews of each style:
[ASCII previews displayed]
Enter the dot style you want (rounded, circle, square_gradient): circle

QR code image saved as 'artistic_qr_code.png'.
ASCII Art QR Code:
[ASCII art displayed]
ASCII art saved as 'artistic_qr_code.txt'.
```

---

## Output Files

- `artistic_qr_code.png`: Styled QR code image.
- `artistic_qr_code.txt`: ASCII art version of the QR code.

---

## Notes

- **vCard Format**: Uses vCard 3.0 with `FN` always included. Other fields (`N`, `ORG`, `TITLE`, `TEL`, `EMAIL`, `NOTE`) are only included if provided and valid.
- **Validation**: Ensures proper formatting for phone numbers and emails.
- **Troubleshooting**:
  - Ensure the script has permission to write files in the working directory.
  - Increase QR size or try a different style if scanning fails.

---

## License

This project is open-source and available under the MIT License.
