import math
import numpy


def GetP(_aX, _aY, _bX, _bY, _pX, _pY):
    ABDistance = math.sqrt((_aX - _bX) * (_aX - _bX) + (_aY - _bY) * (_aY - _bY))
    pointADistance = math.sqrt((_pX - _aX) * (_pX - _aX) + (_pY - _aY) * (_pY - _aY))

    pointA = numpy.array([_aX, _aY])
    pointB = numpy.array([_bX, _bY])
    pointP = numpy.array([_pX, _pY])

    segmentAB = pointB - pointA
    segmentAP = pointP - pointA
    # print('segmentAB : ' + str(segmentAB))
    # print('segmentAP : ' + str(segmentAP))

    area = abs(numpy.cross(segmentAB, segmentAP))
    # print('area : ' + str(area))

    pDistance = area / ABDistance
    # print('pDistance : ' + str(pDistance))

    AXDistance = math.sqrt(pointADistance * pointADistance - pDistance * pDistance)
    # print('AXDistance : ' + str(AXDistance))

    pointX = pointA + segmentAB / ABDistance * AXDistance
    print('pointX : ' + str(pointX))


if __name__ is '__main__':
    # GetP(20.0, 0.0, 0.0, -15.0, 0.0, 0.0)
    pass
