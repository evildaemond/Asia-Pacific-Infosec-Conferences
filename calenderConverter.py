import json
from icalendar import Calendar, Event
from dateutil.parser import parse

# This program is used to parse all of the Asia-Pacific Infosec Conferences into a ".isc" format, so that it can be put inside of your calender program of choice. 

with open('conferenceInfo.json') as confrenceInfo:
    json_confrenceInfo = json.load(confrenceInfo)

# Updated the max range for this each time you add a new entry to the file
for r in range(22):
    # This skips all of the unconfirmed dates for conferences
    if json_confrenceInfo[r]['dateStartDayMonthYear'] =="":
        pass
    else:
        filename = json_confrenceInfo[r]['conferenceName'] + '.ics'
        description = json_confrenceInfo[r]['conferenceName'] + ' ' + 'Attendees: ' + json_confrenceInfo[r]['conferenceAttendees']
        dateStart = parse(json_confrenceInfo[r]['dateStartDayMonthYear'], dayfirst=True)
        dateEnd = parse(json_confrenceInfo[r]['dateEndDayMonthYear'], dayfirst=True)

        cal = Calendar()
        cal.add('prodid', '-//Asia-Pacific-Infosec-Conferences//')
        cal.add('version', '2.0')

        event = Event()
        event.add('summary', json_confrenceInfo[r]['conferenceName'])
        event.add('description', description)
        if json_confrenceInfo[r]['locationStreet'] == "":               # This will check if a venue location has been made
            event.add('location', json_confrenceInfo[r]['location'])    # If it does not exist, it will just select the major city it is located in
        else:
            event.add('location', json_confrenceInfo[r]['locationStreet'])
        event.add('dtstart', dateStart)
        event.add('dtend', dateEnd)
        event.add('dtstamp', dateStart)

        cal.add_component(event)

        f = open(filename, 'wb')
        f.write(cal.to_ical())
        f.close()
        print("Written " + filename + "To Disk")
