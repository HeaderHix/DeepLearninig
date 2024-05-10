from ultralytics import YOLO
import cv2
import math

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Load model
model = YOLO("best.pt")

# Object classes
classNames = ['a4box', 'polybag']

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # Process results
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # Extract bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to integers

            # Choose color based on class
            cls = int(box.cls[0])
            if classNames[cls] == 'a4box':
                color = (0, 0, 255)  # Red
            else: 
                color = (255, 0, 0)  # Blue

            # Draw bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)  # Reduced thickness to 2

            # Display confidence
            confidence = math.ceil(box.conf[0] * 100) / 100
            conf_text = f"Confidence: {confidence:.2f}"
            print("Confidence --->", confidence)
            cv2.putText(img, conf_text, (x1, y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

            # Display class name
            print("Class name -->", classNames[cls])
            cv2.putText(img, classNames[cls], (x1, y1 - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Display image in window
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
