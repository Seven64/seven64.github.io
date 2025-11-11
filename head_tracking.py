# head_tracking.py
# Ein einfaches Beispiel für ein AI-System zur Kopfverfolgung

import cv2  # OpenCV-Bibliothek importieren
import dlib  # Dlib-Bibliothek importieren
import numpy as np  # Numpy-Bibliothek importieren

# Funktion zum Initialisieren des Kopfverfolgers
def initialize_head_tracker():
    # Lade den vorher trainierten Modeller zur Gesichtsverfolgung
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    return detector, predictor

# Hauptfunktion zur Kopfverfolgung
def track_head():
    detector, predictor = initialize_head_tracker()
    
    # Starte die Webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        # Lese einen Frame von der Webcam
        ret, frame = cap.read()
        if not ret:
            break;
            
        # Konvertiere das Bild in Graustufen
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detektiere Gesichter im Frame
        faces = detector(gray)
        
        for face in faces:
            # Zeichne ein Rechteck um das erkannte Gesicht
            x, y, w, h = (face.left(), face.top(), face.width(), face.height())
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Bestimme die Gesichtsmerkmale
            landmarks = predictor(gray, face)
            for n in range(0, 68):
                x_landmark = landmarks.part(n).x
                y_landmark = landmarks.part(n).y
                cv2.circle(frame, (x_landmark, y_landmark), 2, (255, 0, 0), -1)

        # Zeige das Bild mit dem erkannten Gesicht an
        cv2.imshow("Head Tracking", frame)

        # Beende den Prozess bei Drücken der 'q'-Taste
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Freigeben der Ressourcen
    cap.release()
    cv2.destroyAllWindows()

# Starte die Kopfverfolgung
if __name__ == "__main__":
    track_head()