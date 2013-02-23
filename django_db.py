from django_model import *

class DB:
    #InsertTeacher inserts a new teacher into the database and 
    #immediately saves the entry. A new user account is created for the new
    #entry.
    def InsertTeacher(first_name, last_name, school_name, school_addr1,
                        school_addr2, school_city, school_state, school_zip,
                        phone, email, grade, num_students, keywords,
                        password):
        try:
            school = School.get(school_name=school_name, school_zip=school_zip)
        except:
            school = School(school_name, school_addr1, school_addr2, 
                            school_city, school_state, school_zip)
            school.save()
        teacher = Teacher(first_name, last_name, school, phone, email, grade,
                          num_students, keywords)
        teacher.save()

    
    #InsertVolunteer inserts a new volunteer into the database and 
    #immediately saves the entry. A new user account is created for the new
    #entry.
    def InsertVolunteer(first_name, last_name, home_state, country, sector,
                        start_date, end_date, email, language, keywords,
                        password):
        volunteer = Volunteer(first_name, last_name, home_state, country, 
                              sector, start_date, end_date, email, language,
                              keyworks)
        volunteer.save()

    #QueryTeachers returns a list of teachers that fit into all of the 
    #specified search terms. Each element of the list is appropriately 
    #formatted to be rendered on the map. Specifying null for any search term
    #will prohibit any filtering along that category.
    def QueryTeachers(school, state, grade, num_students):
        return 

    #QueryVolunteers returns a list of volunteers that fit into all of the 
    #specified search terms. Each element of the list is appropriately 
    #formatted to be rendered on the map. Specifying null for any search term
    #will prohibit any filtering along that category.
    def QueryVolunteers(countries, sectors, home_states, keywords):
        Volunteer.object.
