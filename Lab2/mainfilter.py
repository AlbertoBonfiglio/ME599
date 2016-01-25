#!/usr/bin/python3

from Lab2.classes.robot import Robot


def main():
    sillyBot = Robot()

    data = sillyBot.getSensorReadings(20, 0.05)
    filterData = sillyBot.filterData(data, 3)
    print(data, filterData)

if __name__ == "__main__":
    main()
