import strings
import dryscrape

class GetDoctorsList(object):

    search_by_to_intervals  = {strings.AREA_OF_TREATMENT:(1, 1)}
    def __init__(self, search_by):
        self.base_url = "http://serguide.maccabi4u.co.il/heb/Doctors/DoctorsSearchResults/"
        self.search_by = search_by
        self.session = dryscrape.session()
        self.search_field_information = {strings.AREA_OF_TREATMENT: (1,1)}

    def search_by_param(self):
        mapping = dict()
        curr_field_xpath = "//section[@id='SearchParams']/span[@class='ng-binding ng-scope']"
        start_point = self.search_field_information[self.search_by][0]
        iterate_by = self.search_field_information[self.search_by][1]
        self.session.visit(self.base_url)
        value_name = self.session.at_xpath("//section[@class=error_section ng-binding ng-scope")

        while value_name == None:
            if(len(self.search_field_information[self.search_by[0]]) == 1):
                start_point = "00" + str(start_point)
            elif (len(self.search_field_information[self.search_by[0]]) == 2):
                start_point = "0" + str(start_point)
            self.session.visit(self.base_url + "?" + self.search_by + start_point)
            value_name = self.session.at_xpath(curr_field_xpath)
            mapping[value_name] = int(start_point)
            start_point += iterate_by

        return mapping





        





