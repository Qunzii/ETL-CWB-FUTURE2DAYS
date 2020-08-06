def get_weather_data(xml, location_, time_):
    all_result = []
    weather_report = xml
    locations = weather_report.find_all("locationname")
    for location in locations:
    # 第一層迴圈先確定地區
        if location.text == location_:
            order = locations.index(location)
            weather_report_modify = weather_report.find_all("location")[order]
            elems = weather_report_modify.find_all("weatherelement")
            for elem in elems:
                weather_element = elem.find("elementname").text
                times = elem.find_all("time")
                if weather_element == "PoP6h" or weather_element == "PoP12h" or weather_element == "Wx" or weather_element == "WeatherDescription":
                    for time in times:
                        start_datatime = time.find("starttime").text
                        if time_ == start_datatime:
                            results = time.find_all("value")
                            for result in results:
                                all_result.append(result.text)
                else:
                    for time in times:
                        start_datatime = time.find("datatime").text
                        if time_ == start_datatime:
                            results = time.find_all("value")
                            for result in results:
                                all_result.append(result.text)

    if all_result == []:
        return all_result

    # 降雨機率如果為空, 轉成0%
    if len(all_result) == 12:
        all_result.insert(3, "")
        all_result.insert(4, "")
    elif len(all_result) == 13:
        all_result.insert(4, "")

    # print("all_result:++++++++++", all_result)
    return all_result