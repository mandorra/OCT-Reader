from struct import unpack
import numpy as np


def getOCTHdr(file):

    # Read binary file
    with open(file, mode='rb') as file:
        fileContent = file.read()

    # Read raw hdr
    Version, SizeX, NumBScans, SizeZ, ScaleX, Distance, ScaleZ, SizeXSlo, SizeYSlo, ScaleXSlo, ScaleYSlo, FieldSizeSlo, ScanFocus, ScanPosition, ExamTime, ScanPattern, BScanHdrSize, ID, ReferenceID, PID, PatientID, Padding, DOB, VID, VisitID, VisitDate, GridType, GridOffset, GridType1, GridOffset1, ProgID, Spare = unpack(
        "=12siiidddiiddid4sQii16s16si21s3sdi24sdiiii34s1790s", fileContent[:2048])

    # Format hdr properly
    hdr = {'Version': Version.rstrip(), 'SizeX': SizeX, 'NumBScans': NumBScans, 'SizeZ': SizeZ, 'ScaleX': ScaleX, 'Distance': Distance, 'ScaleZ': ScaleZ, 'SizeXSlo': SizeXSlo, 'SizeYSlo': SizeYSlo, 'ScaleXSlo': ScaleXSlo, 'ScaleYSlo': ScaleYSlo, 'FieldSizeSlo': FieldSizeSlo, 'ScanFocus': ScanFocus, 'ScanPosition': ScanPosition.rstrip(), 'ExamTime': ExamTime,
           'ScanPattern': ScanPattern, 'BScanHdrSize': BScanHdrSize, 'ID': ID.rstrip(), 'ReferenceID': ReferenceID.rstrip(), 'PID': PID, 'PatientID': PatientID.rstrip(), 'DOB': DOB, 'VID': VID, 'VisitID': VisitID.rstrip(), 'VisitDate': VisitDate, 'GridType': GridType, 'GridOffset': GridOffset, 'GridType1': GridType1, 'GridOffset1': GridOffset1, 'ProgID': ProgID.rstrip()}

    return hdr


def getSLOImage(file, hdr):

    # Read SLO image
    SizeXSlo = hdr['SizeXSlo']
    SizeYSlo = hdr['SizeYSlo']
    SloSize = SizeXSlo * SizeYSlo
    SloOffset = 2048
    SloImg = unpack(
        '=' + str(SloSize) + 'B', fileContent[SloOffset:(SloOffset + SloSize)])
    SloImg = np.asarray(SloImg, dtype='uint8')
    SloImg = SloImg.reshape(SizeXSlo, SizeYSlo)

    return SloImg
