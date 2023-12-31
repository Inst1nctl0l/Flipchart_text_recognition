import sys
import text
import Complex_shape_recognition
import image_preprocessing
from implement_text_rec_for_rus_two_models import recognize_text,recognize_printed_text, recognize_handwritten_text

def main(image_path):
    image_processor = image_preprocessing.ImageProcessing(image_path)
    pre_path = image_processor.process_image()
    handwritten_result = recognize_text(image_path, 'handwritten')
    text.recognize(pre_path)
    Complex_shape_recognition.shape_digitalization(pre_path)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        print("Please provide the image path as a parameter")
        sys.exit(1)
    main(image_path)
'''
(Run the script directly):
python main.py entest.jpg

(Execute code in a Jupyter Notebook or colab or any oyher interactive environment):
import main
main.main('entest.jpg')
'''