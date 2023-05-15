import cv2
import pytesseract

def extract_Alllabels(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

def find_label(image_path, target_label):
    full_text = extract_Alllabels(image_path)
    if target_label in full_text:
        return True
    else:
        return False
      
