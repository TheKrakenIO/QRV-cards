import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask, RadialGradiantColorMask
from PIL import Image, ImageDraw

# Prompt user for vCard information
print("Enter your contact information for the QR code (press Enter to exclude optional fields):")

# Required field: full_name
while True:
    full_name = input("Full Name (required): ").strip()
    if full_name:
        break
    print("Full Name is required. Please enter a valid name.")

# Optional fields
last_name = input("Last Name: ").strip()
first_name = input("First Name: ").strip()
organization = input("Organization: ").strip()
title = input("Job Title: ").strip()
phone = input("Phone Number (e.g., +1234567890): ").strip()
email = input("Email: ").strip()
note = input("Note: ").strip()

# Validate phone number format (only if provided)
if phone and (not phone.startswith("+") or not phone[1:].isdigit()):
    print("Invalid phone number format. Excluding phone from vCard.")
    phone = ""

# Validate email format (only if provided)
if email and "@" not in email:
    print("Invalid email format. Excluding email from vCard.")
    email = ""

# Prompt user for QR code customization (size and output type)
try:
    qr_size = int(input("Enter QR code size in pixels (e.g., 400): "))
    if qr_size <= 0:
        raise ValueError("Size must be positive")
except ValueError:
    print("Invalid size. Using default of 400.")
    qr_size = 400

output_type = input("Output type (image, ascii, or both): ").lower()
if output_type not in ["image", "ascii", "both"]:
    print("Invalid output type. Defaulting to 'image'.")
    output_type = "image"

# Construct vCard with user input (only include non-empty fields except full_name)
vcard_lines = [
    "BEGIN:VCARD",
    "VERSION:3.0",
    f"FN;CHARSET=UTF-8:{full_name}"
]
if last_name or first_name:
    vcard_lines.append(f"N;CHARSET=UTF-8:{last_name};{first_name}")
if organization:
    vcard_lines.append(f"ORG;CHARSET=UTF-8:{organization}")
if title:
    vcard_lines.append(f"TITLE;CHARSET=UTF-8:{title}")
if phone:
    vcard_lines.append(f"TEL:{phone}")
if email:
    vcard_lines.append(f"EMAIL:{email}")
if note:
    vcard_lines.append(f"NOTE;CHARSET=UTF-8:{note}")
vcard_lines.append("END:VCARD")
vcard = "\n".join(vcard_lines)

# Show ASCII previews of dot styles
print("\nChoose a dot style for your QR code. Here are previews of each style:\n")

# Create a small sample QR code for each style to preview
sample_data = "STYLE_PREVIEW"
styles = {
    "rounded": RoundedModuleDrawer(radius_ratio=1),
    "circle": CircleModuleDrawer(),
    "square_gradient": SquareModuleDrawer()
}

for style_name, module_drawer in styles.items():
    if style_name == "square_gradient":
        color_mask = RadialGradiantColorMask(back_color=(255, 255, 255), center_color=(0, 0, 0), edge_color=(100, 100, 100))
    else:
        color_mask = SolidFillColorMask(back_color=(255, 255, 255), front_color=(0, 0, 0))

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
    qr.add_data(sample_data)
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=module_drawer, color_mask=color_mask)

    # Convert to ASCII with scaling for readability
    qr_matrix = qr.get_matrix()
    ascii_art = ""
    for row in qr_matrix:
        for pixel in row:
            if style_name == "rounded":
                ascii_art += "◖◗" if pixel else "  "
            elif style_name == "circle":
                ascii_art += "●●" if pixel else "  "
            elif style_name == "square_gradient":
                ascii_art += "▦▦" if pixel else "  "
        ascii_art += "\n"

    print(f"Style: {style_name}")
    print(ascii_art)
    print()

# Prompt user to choose a style
dot_style = input("Enter the dot style you want (rounded, circle, square_gradient): ").lower()
if dot_style not in ["rounded", "circle", "square_gradient"]:
    print("Invalid dot style. Defaulting to 'rounded'.")
    dot_style = "rounded"

# Calculate box_size based on qr_size 
box_size = max(10, qr_size // 29)  # Ensure minimum box size for readability

# Initialize QR code object with dynamic version
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=box_size,
    border=4,
)

# Add vCard data
qr.add_data(vcard)
qr.make(fit=True)

# Apply the chosen dot style
if dot_style == "rounded":
    module_drawer = RoundedModuleDrawer(radius_ratio=1)
elif dot_style == "circle":
    module_drawer = CircleModuleDrawer()
else:  # square_gradient
    module_drawer = SquareModuleDrawer()

# Choose color mask
if dot_style == "square_gradient":
    color_mask = RadialGradiantColorMask(back_color=(255, 255, 255), center_color=(0, 0, 0), edge_color=(100, 100, 100))
else:
    color_mask = SolidFillColorMask(back_color=(255, 255, 255), front_color=(0, 0, 0))

# Generate the final QR code
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=module_drawer,
    color_mask=color_mask
)

# Add rounded corners
img = img.convert("RGBA")
rounded = Image.new("RGBA", img.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(rounded)
draw.rounded_rectangle(
    (0, 0, img.size[0], img.size[1]),
    radius=40,
    fill=(255, 255, 255, 255)
)
img = Image.composite(img, rounded, rounded)

# Resize to exact qr_size
img = img.resize((qr_size, qr_size), Image.Resampling.LANCZOS)

# Output based on user selection
if output_type in ["image", "both"]:
    try:
        img.save("artistic_qr_code.png", quality=95)
        print("QR code image saved as 'artistic_qr_code.png'.")
    except Exception as e:
        print(f"Failed to save image: {e}")

if output_type in ["ascii", "both"]:
    qr_matrix = qr.get_matrix()
    # Scale down ASCII for large QR codes (sample every nth pixel if matrix is large)
    scale_factor = max(1, len(qr_matrix) // 20)  # Limit to ~20x20 for ASCII
    ascii_art = ""
    for i in range(0, len(qr_matrix), scale_factor):
        row = qr_matrix[i]
        for j in range(0, len(row), scale_factor):
            pixel = row[j]
            if dot_style == "rounded":
                ascii_art += "◖◗" if pixel else "  "
            elif dot_style == "circle":
                ascii_art += "●●" if pixel else "  "
            else:  # square_gradient
                ascii_art += "▦▦" if pixel else "  "
        ascii_art += "\n"
    print("ASCII Art QR Code:\n")
    print(ascii_art)
    try:
        with open("artistic_qr_code.txt", "w", encoding="utf-8") as f:
            f.write(ascii_art)
        print("ASCII art saved as 'artistic_qr_code.txt'.")
    except Exception as e:
        print(f"Failed to save ASCII art: {e}")
