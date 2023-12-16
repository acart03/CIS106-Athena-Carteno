class Car:
  def __init__(self, Make, Model, Year, StickerPrice):
     self.Make = Make
     self.Model = Model
     self.Year = Year
     self.StickerPrice = StickerPrice
     self.DiscountPrice = StickerPrice * .9
     self.UpdatedPrice = 0

  def longname(self):
    return "{} {} {}".format(self.Year, self.Make, self.Model)


class Sport(Car):
  def __init__(self, Make, Model, Year, StickerPrice, SportWheels, SportEngine, SportInterior):
     self.Make = Make
     self.Model = Model
     self.Year = Year
     self.StickerPrice = StickerPrice
     self.DiscountPrice = StickerPrice * .9
     self.SportWheels = SportWheels
     self.SportInterior = SportInterior
     self.SportEngine = SportEngine
     self.UpdatedPrice = 0

  def pricewithoptions(self, SportWheels, SportEngine, SportInterior, DiscountPrice):
    if SportWheels == "y":
      UpdatedPrice = DiscountPrice + 1000.00
    else:
      UpdatedPrice = DiscountPrice
    if SportEngine == "y":
      UpdatedPrice = UpdatedPrice + 3000.00
    else:
      UpdatedPrice = UpdatedPrice
    if SportInterior == "y":
      UpdatedPrice = UpdatedPrice + 2000.00
    else:
      UpdatedPrice = UpdatedPrice
    return UpdatedPrice



CarOne = Sport('Nissan', 'Altima', 2006, 3000.00,'n', 'y', 'y',)
CarTwo = Sport('Toyota', 'RAV4', 2012, 14000.00,'n', 'y', 'n',)
CarThree = Sport('Honda', 'Accord', 2018, 30000.00,'y', 'y', 'y',)
print( "Car: ", CarOne.longname())
print("Sticker price: $", CarOne.StickerPrice)
print("Discounted price: $", CarOne.DiscountPrice)

print("Price with added options: $", CarOne.pricewithoptions(CarOne.SportWheels, CarOne.SportEngine, 
                                                             CarOne.SportInterior, CarOne.DiscountPrice))
print("")
print( "Car: ", CarTwo.longname())
print("Sticker price: $", CarTwo.StickerPrice)
print("Discounted price: $", CarTwo.DiscountPrice)

print("Price with added options: $", CarTwo.pricewithoptions(CarTwo.SportWheels, CarTwo.SportEngine, 
                                                             CarTwo.SportInterior, CarTwo.DiscountPrice))
print("")
print( "Car: ", CarThree.longname())
print("Sticker price: $", CarThree.StickerPrice)
print("Discounted price: $", CarThree.DiscountPrice)
print("Price with added options: $", CarThree.pricewithoptions(CarThree.SportWheels, CarThree.SportEngine, 
                                                               CarThree.SportInterior, CarThree.DiscountPrice))
print("")