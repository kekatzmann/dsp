

faculty_dict = {}
faculty_dict['Ellenberg'] = [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']]
faculty_dict['Li'] = [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]


dict_d = {...}
for key in sorted(faculty_dict)[:3]:
    print (key, faculty_dict[key])

professor_dict = {}
professor_dict['Susan', 'Ellenberg'] = ['Ph.D.', 'Professor', 'sellenbe@upenn.edu']
professor_dict['Jonas', 'Ellenberg'] = ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
professor_dict['Yimei', 'Li'] = ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu']
professor_dict['Mingyao','Li'] = ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu']
professor_dict['Hongzhe','Li'] = ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']

for key in sorted(professor_dict)[:3]:
    print (key, professor_dict[key])

for key in sorted(professor_dict, key = lambda x: x[1])[:3]:
    print (key, professor_dict[key])
