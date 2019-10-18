import exifread
from geopy.geocoders import Nominatim


def getImageExt(path):
  """get image exit : time and gps"""
  img = exifread.process_file(open(path, 'rb'))
  try:
    time = img['Image DateTime']
    latitude = img['GPS GPSLatitude']
    longitude = img['GPS GPSLongitude']
    return (time, latitude, longitude)
  except KeyError:
    print("get image ext error")
    return (None, None, None)


def formatLatiLong(data):
  """format gps to str"""
  listTmp = str(data).replace('[', '').replace(']', '').split(',')
  list = [ele.strip() for ele in listTmp]
  if list[-1].find('/') > 0:
    dataSec = int(list[-1].split('/')[0]) / (int(list[-1].split('/')[1]) * 3600)
  else:
    dataSec = (int)(list[-1])

  dataMinute = int(list[1]) / 60
  dataDegree = int(list[0])
  return dataDegree + dataMinute + dataSec


def convertToAddress(lat, lon):
  """get addresss from gps"""
  geolocator = Nominatim()
  position = geolocator.reverse(
      '{lat},{lon}'.format(lat=lat, lon=lon), timeout=10)
  return position.address


def analysisImage(path):
  (time, latitude, longitude) = getImageExt(path)
  if time and latitude and longitude:
    address = convertToAddress(
        formatLatiLong(latitude), formatLatiLong(longitude))
    return (time, address)
  return (None, None)
