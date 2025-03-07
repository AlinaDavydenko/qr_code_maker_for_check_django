import qrcode
import qrcode.image.base
import qrcode.image.pil


def make_qr_code(path_to_pdf, path_to_qr):
    """ формирование qr_code по указанному пути """
    qr_code = qrcode.make(path_to_pdf, box_size=10, border=1)
    qr_code.save(path_to_qr)
    return qr_code
