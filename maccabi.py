import strings
import dryscrape


class ParamMapper(object):
    search_by_to_intervals = {strings.AREA_OF_TREATMENT: (1, 1)}

    def __init__(self, search_by):
        self.base_url = "http://serguide.maccabi4u.co.il/heb/Doctors/DoctorsSearchResults/"
        self.search_by = search_by
        self.session = dryscrape.Session()
        self.search_field_information = {strings.AREA_OF_TREATMENT: (1, 1)}

    def map_param(self):
        mapping = dict()
        curr_field_xpath = "//section[@id='SearchParams']/span[@class='ng-binding ng-scope']"
        start_point, iterate_by = self.search_field_information[self.search_by]
        value_name = self.session.at_xpath("//section[@class=error_section ng-binding ng-scope")

        while value_name is None:
            self.session.visit("%s?%s%s" % (self.base_url, self.search_by, str(start_point).zfill(3)))
            value_name = self.session.at_xpath(curr_field_xpath)
            mapping[value_name] = start_point
            start_point += iterate_by

        return mapping


def main():
    mapper = ParamMapper(strings.AREA_OF_TREATMENT)
    mapping = mapper.map_param()
    print(mapping)


if __name__ == '__main__':
    main()
