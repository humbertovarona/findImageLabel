image_path = './sample.jpeg'
target_label = 'Anomaly'


txt = extract_Alllabels(image_path)
label_found = find_label(image_path, target_label)

if label_found:
    print("Label found in the image!")
    print(txt)
else:
    print("Label not found in the image.")
    
