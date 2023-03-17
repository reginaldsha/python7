from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

# window instance
window = Tk()
style=ttk.Style()
window.title("EWEN CHARITY MANAGEMENT SOFTWARE")
window.geometry("1650x1000")

def add_1():
    a = entry_0.get()
    b = entry_1.get()
    c = entry_2.get()
    d = entry_3.get()
    e = entry_4.get()
    f = entry_5.get()
    if a == "" or b == "" or c == "" or d == "" or e == "" or f == "" :
        MessageBox.showinfo("insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="volunteer_management")
        cursor = con.cursor()
        cursor.execute(
            "insert into volunteer_management.roleperson_data (firstname,lastname,homeaddress,contact,email,role)values('" + a + "','" + b + "','" + c + "','" + d + "','" + e + "','" + f + "')")
        con.commit()

        entry_0.delete(0, END)
        entry_1.delete(0, END)
        entry_2.delete(0, END)
        entry_3.delete(0, END)
        entry_4.delete(0, END)
        entry_5.delete(0, END)



        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()


def add_2():
    g = entry_6.get()
    h = entry_7.get()
    i = entry_8.get()
    j = entry_9.get()

    if g == "" or h == "" or i == "" or j == "":
        MessageBox.showinfo("insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="logistics")
        cursor = con.cursor()
        cursor.execute(
            "insert into logistics.logistics_services (event,description_event,contact_event,email_event)values('" + g + "','" + h + "','" + i + "','" + j + "')")
        con.commit()

        entry_6.delete(0, END)
        entry_7.delete(0, END)
        entry_8.delete(0, END)
        entry_9.delete(0, END)


        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()


def add_3():
    k = entry_10.get()
    o = entry_11.get()
    m = entry_12.get()
    n = entry_13.get()

    if k == "" or o == "" or m == "" or n == "":
        MessageBox.showinfo("insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="logistics")
        cursor = con.cursor()
        cursor.execute(
            "insert into logistics.transport (taxi,taxi_descript,taxi_contact,taxi_email)values('" + k + "','" + o + "','" + m + "','" + n + "')")
        con.commit()

        entry_10.delete(0, END)
        entry_11.delete(0, END)
        entry_12.delete(0, END)
        entry_13.delete(0, END)


        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()


def add_4():
    q = entry_14.get()
    r = entry_15.get()
    s = entry_16.get()
    t = entry_17.get()

    if q == "" or r == "" or s == "" or t == "":
        MessageBox.showinfo("insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
        cursor = con.cursor()
        cursor.execute(
            "insert into hr_resource.entertainment (ent_agency,ent_descript,ent_contact,ent_email)values('" + q + "','" + r + "','" + s + "','" + t + "')")
        con.commit()

        entry_14.delete(0, END)
        entry_15.delete(0, END)
        entry_16.delete(0, END)
        entry_17.delete(0, END)


        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()


def add_5():
    u = entry_18.get()
    v = entry_19.get()
    w = entry_20.get()
    s = entry_21.get()

    if u == "" or v == "" or w == "" or s == "":
        MessageBox.showinfo("insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
        cursor = con.cursor()
        cursor.execute(
            "insert into hr_resource.event_staffA (estaff_agency,estaff_descript,estaff_contact,estaff_email)values('" + u + "','" + v + "','" + w + "','" + s + "')")
        con.commit()

        entry_18.delete(0, END)
        entry_19.delete(0, END)
        entry_20.delete(0, END)
        entry_21.delete(0, END)


        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()


def add_6():
    aa = entry_22.get()
    bb = entry_23.get()
    cc = entry_24.get()
    dd = entry_25.get()

    if aa == "" or bb == "" or cc == "" or dd == "":
        MessageBox.showinfo("insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
        cursor = con.cursor()
        cursor.execute(
            "insert into hr_resource.security_cpm (security_comp,securicmp_descript,securitycmp_contact,securitycmp_email)values('" + aa + "','" + bb + "','" + cc + "','" + dd + "')")
        con.commit()

        entry_22.delete(0, END)
        entry_23.delete(0, END)
        entry_24.delete(0, END)
        entry_25.delete(0, END)


        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()



def add_7():
    ab = entry_26.get()
    bc = entry_27.get()
    cd = entry_28.get()
    de = entry_29.get()

    if ab == "" or bc == "" or cd == "" or de == "":
        MessageBox.showinfo("insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
        cursor = con.cursor()
        cursor.execute(
            "insert into hr_resource.hotels (hotel,hotel_descript,hotel_contact,hotel_email)values('" + ab + "','" + bc + "','" + cd + "','" + de + "')")
        con.commit()

        entry_26.delete(0, END)
        entry_27.delete(0, END)
        entry_28.delete(0, END)
        entry_29.delete(0, END)


        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()



def show():
    con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="volunteer_management")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM  volunteer_management.roleperson_data ")
    rows = cursor.fetchall()
    my_tree_1.delete(*my_tree_1.get_children())
    global count
    count = 0

    for row in rows:
        my_tree_1.insert(parent='',index='end',iid=count,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        count+=1
    con.commit()
    con.close()


# event logistics callback

def show_1():
    con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="logistics")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM  logistics.logistics_services ")
    rows = cursor.fetchall()
    my_tree_2.delete(*my_tree_2.get_children())

    global count
    count = 0

    for row in rows:
        my_tree_2.insert(parent='',index='end',iid=count,text='',values=(row[0],row[1],row[2],row[3],row[4]))
        count+=1

    con.commit()
    con.close()


#taxi logistics callback
def show_2():
    con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="logistics")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM  logistics.transport")
    rows = cursor.fetchall()
    my_tree_3.delete(*my_tree_3.get_children())
    global count
    count = 0

    for row in rows:
        my_tree_3.insert(parent='',index='end',iid=count,text='',values=(row[0],row[1],row[2],row[3],row[4]))
        count+=1
    con.commit()
    con.close()

# entertainment agencies callback
def show_3():
    con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM  hr_resource.entertainment")
    rows = cursor.fetchall()
    my_tree_4.delete(*my_tree_4.get_children())
    global count
    count = 0

    for row in rows:
        my_tree_4.insert(parent='',index='end',iid=count,text='',values=(row[0],row[1],row[2],row[3],row[4]))
        count+=1

    con.commit()
    con.close()



# staffing agency callbacks

def show_4():
    con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM  hr_resource.event_staffA")
    rows = cursor.fetchall()
    my_tree_5.delete(*my_tree_5.get_children())
    global count
    count = 0

    for row in rows:
        my_tree_5.insert(parent='',index='end',iid=count,text='',values=(row[0],row[1],row[2],row[3],row[4]))
        count+=1
    con.commit()
    con.close()

# security companies callbacks

def show_5():
    con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM  hr_resource.security_cpm")
    rows = cursor.fetchall()
    my_tree_6.delete(*my_tree_6.get_children())
    global count
    count = 0

    for row in rows:
        my_tree_6.insert(parent='',index='end',iid=count,text='',values=(row[0],row[1],row[2],row[3],row[4]))
        count+=1
    con.commit()
    con.close()

#hotels call back
def show_6():
    con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM  hr_resource.hotels")
    rows = cursor.fetchall()
    my_tree_7.delete(*my_tree_7.get_children())
    global count
    count = 0

    for row in rows:
        my_tree_7.insert(parent='',index='end',iid=count,text='',values=(row[0],row[1],row[2],row[3],row[4]))
        count+=1
    con.commit()
    con.close()

#delete record from volunteer management
def vm_del():
    if(vmp_entry.get() == ""):
        MessageBox.showinfo("Delete Status", "Record No is compulsory for Delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="volunteer_management")
        cursor = con.cursor()
        cursor.execute("DELETE FROM  volunteer_management.roleperson_data WHERE person_id ='" + vmp_entry.get() + "'" )
        con.commit()

        vmp_entry.delete(0, END)


        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()
# update callback for volunteer management
def vm_updat():
    a = rec_no_entry.get()
    b = first_no_entry.get()
    c = last_no_entry.get()
    d = hom_no_entry.get()
    e = cont_no_entry.get()
    f = mail_no_entry.get()
    g = role_no_entry.get()

    if a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "":
        MessageBox.showinfo("Update status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="volunteer_management")
        cursor = con.cursor()
        cursor.execute(
            "UPDATE volunteer_management.roleperson_data  SET firstname = '" + b + "', lastname ='" + c + "', homeaddress = '" + d + "',contact = '" + e + "', email = '" + f + "', role = '" + g + "' WHERE person_id = '" + a + "'")
        con.commit()

        rec_no_entry.delete(0, END)
        first_no_entry.delete(0, END)
        last_no_entry.delete(0, END)
        hom_no_entry.delete(0, END)
        cont_no_entry.delete(0, END)
        mail_no_entry.delete(0, END)
        role_no_entry.delete(0, END)


        MessageBox.showinfo("Update Status", "Updated Successfully")
        con.close()


#delete record from Event logistics record
def elog_del():
    if(evt_entry.get() == ""):
        MessageBox.showinfo("Delete Status", "Record No is compulsory for Delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="logistics")
        cursor = con.cursor()
        cursor.execute("DELETE FROM  logistics.logistics_services WHERE event_number ='" + evt_entry.get() + "'" )
        con.commit()

        evt_entry.delete(0, END)


        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()


#delete record from taxi record
def eTax_del():
    if(taxi_entry.get() == ""):
        MessageBox.showinfo("Delete Status", "Record No is compulsory for Delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="logistics")
        cursor = con.cursor()
        cursor.execute("DELETE FROM  logistics.transport WHERE taxi_no ='" + taxi_entry.get() + "'" )
        con.commit()

        taxi_entry.delete(0, END)


        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()

#update callback for event logistics services
def levt_updat():
    a_1 = evt_no_entry.get()
    b_2 = elsl_no_entry.get()
    c_3 = desc_no_entry.get()
    d_4 = contlog_no_entry.get()
    e_5 = maillog_no_entry.get()


    if a_1 == "" or b_2 == "" or c_3 == "" or d_4 == "" or e_5 == "" :
        MessageBox.showinfo("Update status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="logistics")
        cursor = con.cursor()
        cursor.execute(
            "UPDATE logistics.logistics_services  SET event = '" + b_2 + "', description_event ='" + c_3 + "', contact_event = '" + d_4 + "',email_event = '" + e_5 + "' WHERE event_number = '" + a_1 + "'")
        con.commit()

        evt_no_entry.delete(0, END)
        elsl_no_entry.delete(0, END)
        desc_no_entry.delete(0, END)
        contlog_no_entry.delete(0, END)
        maillog_no_entry.delete(0, END)


        MessageBox.showinfo("Update Status", "Updated Successfully")
        con.close()


# update callback for taxi
def taxxi_updat():
    a_6 = tax_no_entry.get()
    b_7 = taxi_no_entry.get()
    c_8 = taxii_no_entry.get()
    d_9 = conttax_no_entry.get()
    e_10 = mailtax_no_entry.get()


    if a_6 == "" or b_7 == "" or c_8 == "" or d_9 == "" or e_10 == "" :
        MessageBox.showinfo("Update status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="logistics")
        cursor = con.cursor()
        cursor.execute(
            "UPDATE logistics.transport  SET event = '" + b_7 + "', description_event ='" + c_8 + "', contact_event = '" + d_9 + "',email_event = '" + e_10 + "' WHERE taxi_no = '" + a_6 + "'")
        con.commit()

        tax_no_entry.delete(0, END)
        taxi_no_entry.delete(0, END)
        taxii_no_entry.delete(0, END)
        conttax_no_entry.delete(0, END)
        mailtax_no_entry.delete(0, END)


        MessageBox.showinfo("Update Status", "Updated Successfully")
        con.close()

#delete record from entertainment agencies in london record
def eal_del():
    if(ent_entry.get() == ""):
        MessageBox.showinfo("Delete Status", "Record No is compulsory for Delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
        cursor = con.cursor()
        cursor.execute("DELETE FROM  hr_resource.entertainment WHERE ent_no ='" + ent_entry.get() + "'" )
        con.commit()

        ent_entry.delete(0, END)


        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()

#delete record from event staffing  agencies
def event_staff_del():
    if(estaff_entry.get() == ""):
        MessageBox.showinfo("Delete Status", "Record No is compulsory for Delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
        cursor = con.cursor()
        cursor.execute("DELETE FROM  hr_resource.event_staffA WHERE estaffa_no ='" + estaff_entry.get() + "'" )
        con.commit()

        estaff_entry.delete(0, END)


        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()


# update callback for entertainment agencies in london
def eAL_updat():
    a_11 = ent_no_entry.get()
    b_12 = enta_no_entry.get()
    c_13 = descent_ent_entry.get()
    d_14 = contlogent_no_entry.get()
    e_15 = maillent_no_entry.get()


    if a_11 == "" or b_12 == "" or c_13 == "" or d_14 == "" or e_15 == "" :
        MessageBox.showinfo("Update status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
        cursor = con.cursor()
        cursor.execute(
            "UPDATE hr_resource.entertainment  SET event = '" + b_12 + "', description_event ='" + c_13 + "', contact_event = '" + d_14 + "',email_event = '" + e_15 + "' WHERE ent_no = '" + a_11 + "'")
        con.commit()

        ent_no_entry.delete(0, END)
        enta_no_entry.delete(0, END)
        descent_ent_entry.delete(0, END)
        contlogent_no_entry.delete(0, END)
        maillent_no_entry.delete(0, END)


        MessageBox.showinfo("Update Status", "Updated Successfully")
        con.close()


# update callback for event staffing agencies in london
def etaff_updat():
    a_16 = staff_no_entry.get()
    b_17 = sta_no_entry.get()
    c_18 = staffd_no_entry.get()
    d_19 = contstaff_no_entry.get()
    e_20 = mailstaff_no_entry.get()


    if a_16 == "" or b_17 == "" or c_18 == "" or d_19 == "" or e_20 == "" :
        MessageBox.showinfo("Update status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
        cursor = con.cursor()
        cursor.execute(
            "UPDATE hr_resource.event_staffA  SET estaff_agency = '" + b_17 + "', estaff_descript ='" + c_18 + "', estaff_contact = '" + d_19 + "',estaff_email = '" + e_20 + "' WHERE estaffa_no = '" + a_16 + "'")
        con.commit()

        staff_no_entry.delete(0, END)
        sta_no_entry.delete(0, END)
        staffd_no_entry.delete(0, END)
        contstaff_no_entry.delete(0, END)
        mailstaff_no_entry.delete(0, END)


        MessageBox.showinfo("Update Status", "Updated Successfully")
        con.close()

#delete record from security company
def security_comp_del():
    if(sec_entry.get() == ""):
        MessageBox.showinfo("Delete Status", "Record No is compulsory for Delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
        cursor = con.cursor()
        cursor.execute("DELETE FROM  hr_resource.security_cpm WHERE securitycmp_no ='" + sec_entry.get() + "'" )
        con.commit()

        sec_entry.delete(0, END)


        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()

#delete record from hotels
def hotel_comp_del():
    if(hot_entry.get() == ""):
        MessageBox.showinfo("Delete Status", "Record No is compulsory for Delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
        cursor = con.cursor()
        cursor.execute("DELETE FROM  hr_resource.hotels WHERE hotel_no ='" + hot_entry.get() + "'" )
        con.commit()

        hot_entry.delete(0, END)


        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()

# update callback for security companies
def security_updat():
    a_21 = s_no_entry.get()
    b_22 = sn_no_entry.get()
    c_23 = sndes_ent_entry.get()
    d_24 = sncont_no_entry.get()
    e_25 = maillsnc_no_entry.get()


    if a_21 == "" or b_22 == "" or c_23 == "" or d_24 == "" or e_25 == "" :
        MessageBox.showinfo("Update status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
        cursor = con.cursor()
        cursor.execute(
            "UPDATE hr_resource.security_cpm  SET security_comp = '" + b_22 + "', securitycmp_descript ='" + c_23 + "', securitycmp_contact = '" + d_24 + "',securitycmp_email = '" + e_25 + "' WHERE securitycmp_no = '" + a_21 + "'")
        con.commit()

        s_no_entry.delete(0, END)
        sn_no_entry .delete(0, END)
        sndes_ent_entry.delete(0, END)
        sncont_no_entry.delete(0, END)
        maillsnc_no_entry.delete(0, END)


        MessageBox.showinfo("Update Status", "Updated Successfully")
        con.close()


# update callback for hotels
def hotely_updat():
    a_21 = htl_no_entry.get()
    b_22 = htln.get()
    c_23 = staffd_no_entry.get()
    d_24 = conthtlentry.get()
    e_25 =mailhtl_no_entry .get()


    if a_21 == "" or b_22 == "" or c_23 == "" or d_24 == "" or e_25 == "" :
        MessageBox.showinfo("Update status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="hr_resource")
        cursor = con.cursor()
        cursor.execute(
            "UPDATE hr_resource.hotels  SET hotel = '" + b_22 + "', hotel_descript ='" + c_23 + "', hotel_contact = '" + d_24 + "',hotel_email = '" + e_25 + "' WHERE hotel_no = '" + a_21 + "'")
        con.commit()

        htl_no_entry.delete(0, END)
        htln .delete(0, END)
        staffd_no_entry.delete(0, END)
        conthtlentry.delete(0, END)
        mailhtl_no_entry.delete(0, END)


        MessageBox.showinfo("Update Status", "Updated Successfully")
        con.close()












# Tab creation
tabsystem = ttk.Notebook(window)
tab1=Frame(tabsystem,bg="light blue")
tab2=Frame(tabsystem,bg="light yellow")
tab3=Frame(tabsystem,bg="yellow")
tab4=Frame(tabsystem,bg="light green")
tab5=Frame(tabsystem,bg="orange")
tab6=Frame(tabsystem,bg="green")
tab7=Frame(tabsystem,bg="purple")

tabsystem.add(tab1,text="New data volunteer management")
tabsystem.add(tab2,text="New data logistics ")
tabsystem.add(tab3,text="New data HR resource")
tabsystem.add(tab4,text="Volunteer management data display ")
tabsystem.add(tab5,text="logistics data display")
tabsystem.add(tab6,text="HR-1 data display ")
tabsystem.add(tab7,text="HR-2 data display")


tabsystem.pack(expand=1,fill="both")
style.configure('TNotebook.Tab', font=('URW Gothic L','11','bold') )

# creation of volunteer management labelframe
vmlabel=LabelFrame(tab1,text="Add entries to volunteer management",fg="blue",font="bold")
vmlabel.place(x=20,y=20,width=750,height=280)

# creation of wicgets and placing on  volunteer management labelframe
label_0=Label(vmlabel,text="firstname",font=('ariel 12 bold'),fg="black")
label_0.place(x=0,y=40,width=150,height=20)
entry_0=Entry(vmlabel,borderwidth=1.5)
entry_0.place(x=200,y=40,width=200,height=20)

label_1=Label(vmlabel,text="lastname",font=('ariel 12 bold'),fg="black")
label_1.place(x=0,y=70,width=150,height=20)
entry_1=Entry(vmlabel,borderwidth=1.5)
entry_1.place(x=200,y=70,width=200,height=20)

label_2=Label(vmlabel,text="home-address",font=('ariel 12 bold'),fg="black")
label_2.place(x=0,y=100,width=150,height=20)
entry_2=Entry(vmlabel,borderwidth=1.5)
entry_2.place(x=200,y=100,width=500,height=20)

label_3=Label(vmlabel,text="contact",font=('ariel 12 bold'),fg="black")
label_3.place(x=0,y=130,width=150,height=20)
entry_3=Entry(vmlabel,borderwidth=1.5)
entry_3.place(x=200,y=130,width=200,height=20)

label_4=Label(vmlabel,text="email",font=('ariel 12 bold'),fg="black")
label_4.place(x=0,y=160,width=150,height=20)
entry_4=Entry(vmlabel,borderwidth=1.5)
entry_4.place(x=200,y=160,width=200,height=20)

label_5=Label(vmlabel,text="role",font=('ariel 12 bold'),fg="black")
label_5.place(x=0,y=190,width=150,height=20)
entry_5=Entry(vmlabel,borderwidth=1.5)
entry_5.place(x=200,y=190,width=200,height=20)
addbutton_1=Button(vmlabel,text="Add Record",font=('ariel 14 bold'),fg="blue",command=add_1)
addbutton_1.place(x=200,y=220,width=150,height=30)

# labelframe and widgets on logistics tab
log1label_1=LabelFrame(tab2,text="Add entries to event logistics services in london",fg="blue",font="bold")
log1label_1.place(x=20,y=20,width=750,height=280)

label_6=Label(log1label_1,text="Event logistics services",font=('ariel 12 bold'),fg="black")
label_6.place(x=0,y=40,width=180,height=20)
entry_6=Entry(log1label_1,borderwidth=0.5)
entry_6.place(x=200,y=40,width=200,height=20)

label_7=Label(log1label_1,text="description",font=('ariel 12 bold'),fg="black")
label_7.place(x=0,y=70,width=200,height=20)
entry_7=Entry(log1label_1)
entry_7.place(x=200,y=70,width=500,height=20)

label_8=Label(log1label_1,text="contact",font=('ariel 12 bold'),fg="black")
label_8.place(x=0,y=100,width=150,height=20)
entry_8=Entry(log1label_1)
entry_8.place(x=200,y=100,width=200,height=20)

label_9=Label(log1label_1,text="email",font=('ariel 12 bold'),fg="black")
label_9.place(x=0,y=130,width=150,height=20)
entry_9=Entry(log1label_1)
entry_9.place(x=200,y=130,width=200,height=20)

addbutton_2=Button(log1label_1,text="Add Record",font=('ariel 14 bold'),fg="blue",command=add_2)
addbutton_2.place(x=200,y=220,width=150,height=30)

# taxi labelframe
log2label_1=LabelFrame(tab2,text="Add entries to taxi's",fg="blue",font="bold")
log2label_1.place(x=20,y=350,width=750,height=280)

label_10=Label(log2label_1,text="Taxi",font=('ariel 12 bold'),fg="black")
label_10.place(x=0,y=40,width=180,height=20)
entry_10=Entry(log2label_1,borderwidth=0.5)
entry_10.place(x=200,y=40,width=200,height=20)

label_11=Label(log2label_1,text="description",font=('ariel 12 bold'),fg="black")
label_11.place(x=0,y=70,width=200,height=20)
entry_11=Entry(log2label_1)
entry_11.place(x=200,y=70,width=500,height=20)

label_12=Label(log2label_1,text="contact",font=('ariel 12 bold'),fg="black")
label_12.place(x=0,y=100,width=150,height=20)
entry_12=Entry(log2label_1)
entry_12.place(x=200,y=100,width=200,height=20)

label_13=Label(log2label_1,text="email",font=('ariel 12 bold'),fg="black")
label_13.place(x=0,y=130,width=150,height=20)
entry_13=Entry(log2label_1)
entry_13.place(x=200,y=130,width=200,height=20)

addbutton_3=Button(log2label_1,text="Add Record",font=('ariel 14 bold'),fg="blue",command=add_3)
addbutton_3.place(x=200,y=220,width=150,height=30)

# entertainment labelframe on hrresource tab
log3label_1=LabelFrame(tab3,text="Add entries to entertainment agencies in London",fg="blue",font="bold")
log3label_1.place(x=20,y=20,width=750,height=260)


label_14=Label(log3label_1,text="Entertainment agencies",font=('ariel 12 bold'),fg="black")
label_14.place(x=0,y=40,width=180,height=20)
entry_14=Entry(log3label_1,borderwidth=0.5)
entry_14.place(x=200,y=40,width=200,height=20)

label_15=Label(log3label_1,text="description",font=('ariel 12 bold'),fg="black")
label_15.place(x=0,y=70,width=200,height=20)
entry_15=Entry(log3label_1)
entry_15.place(x=200,y=70,width=500,height=20)

label_16=Label(log3label_1,text="contact",font=('ariel 12 bold'),fg="black")
label_16.place(x=0,y=100,width=150,height=20)
entry_16=Entry(log3label_1)
entry_16.place(x=200,y=100,width=200,height=20)

label_17=Label(log3label_1,text="email",font=('ariel 12 bold'),fg="black")
label_17.place(x=0,y=130,width=150,height=20)
entry_17=Entry(log3label_1)
entry_17.place(x=200,y=130,width=200,height=20)

addbutton_4=Button(log3label_1,text="Add Record",font=('ariel 14 bold'),fg="blue",command=add_4)
addbutton_4.place(x=200,y=190,width=150,height=30)

#event staffing agencies label frame on hr-resource tab
log4label_1=LabelFrame(tab3,text="Add entries to event staffing agencies in London",fg="blue",font="bold")
log4label_1.place(x=20,y=300,width=750,height=260)


label_18=Label(log4label_1,text="Staffing agencies",font=('ariel 12 bold'),fg="black")
label_18.place(x=0,y=40,width=180,height=20)
entry_18=Entry(log4label_1,borderwidth=0.5)
entry_18.place(x=200,y=40,width=200,height=20)

label_19=Label(log4label_1,text="description",font=('ariel 12 bold'),fg="black")
label_19.place(x=0,y=70,width=200,height=20)
entry_19=Entry(log4label_1)
entry_19.place(x=200,y=70,width=500,height=20)

label_20=Label(log4label_1,text="contact",font=('ariel 12 bold'),fg="black")
label_20.place(x=0,y=100,width=150,height=20)
entry_20=Entry(log4label_1)
entry_20.place(x=200,y=100,width=200,height=20)

label_21=Label(log4label_1,text="email",font=('ariel 12 bold'),fg="black")
label_21.place(x=0,y=130,width=150,height=20)
entry_21=Entry(log4label_1)
entry_21.place(x=200,y=130,width=200,height=20)

addbutton_5=Button(log4label_1,text="Add Record",font=('ariel 14 bold'),fg="blue",command=add_5)
addbutton_5.place(x=200,y=190,width=150,height=30)

#security companies  label frame on hr-resource tab
log5label_1=LabelFrame(tab3,text="Add entries to security companies",fg="blue",font="bold")
log5label_1.place(x=800,y=20,width=750,height=260)

label_22=Label(log5label_1,text="Security company",font=('ariel 12 bold'),fg="black")
label_22.place(x=0,y=40,width=180,height=20)
entry_22=Entry(log5label_1,borderwidth=0.5)
entry_22.place(x=200,y=40,width=200,height=20)

label_23=Label(log5label_1,text="description",font=('ariel 12 bold'),fg="black")
label_23.place(x=0,y=70,width=200,height=20)
entry_23=Entry(log5label_1)
entry_23.place(x=200,y=70,width=500,height=20)

label_24=Label(log5label_1,text="contact",font=('ariel 12 bold'),fg="black")
label_24.place(x=0,y=100,width=150,height=20)
entry_24=Entry(log5label_1)
entry_24.place(x=200,y=100,width=200,height=20)

label_25=Label(log5label_1,text="email",font=('ariel 12 bold'),fg="black")
label_25.place(x=0,y=130,width=150,height=20)
entry_25=Entry(log5label_1)
entry_25.place(x=200,y=130,width=200,height=20)

addbutton_6=Button(log5label_1,text="Add Record",font=('ariel 14 bold'),fg="blue",command=add_6)
addbutton_6.place(x=200,y=190,width=150,height=30)

# hotels label frame on hr resource tab
log6label_1=LabelFrame(tab3,text="Add entries to Hotels ",fg="blue",font="bold")
log6label_1.place(x=800,y=300,width=750,height=260)

label_26=Label(log6label_1,text="hotel",font=('ariel 12 bold'),fg="black")
label_26.place(x=0,y=40,width=180,height=20)
entry_26=Entry(log6label_1,borderwidth=0.5)
entry_26.place(x=200,y=40,width=200,height=20)

label_27=Label(log6label_1,text="description",font=('ariel 12 bold'),fg="black")
label_27.place(x=0,y=70,width=200,height=20)
entry_27=Entry(log6label_1)
entry_27.place(x=200,y=70,width=500,height=20)

label_28=Label(log6label_1,text="contact",font=('ariel 12 bold'),fg="black")
label_28.place(x=0,y=100,width=150,height=20)
entry_28=Entry(log6label_1)
entry_28.place(x=200,y=100,width=200,height=20)

label_29=Label(log6label_1,text="email",font=('ariel 12 bold'),fg="black")
label_29.place(x=0,y=130,width=150,height=20)
entry_29=Entry(log6label_1)
entry_29.place(x=200,y=130,width=200,height=20)

addbutton_7=Button(log6label_1,text="Add Record",font=('ariel 14 bold'),fg="blue",command=add_7)
addbutton_7.place(x=200,y=190,width=150,height=30)



# Tree view display wicgets for volunteer management
#my_tree_1 = ttk.Treeview(tab4)

tree_frame=Frame(tab4)
tree_frame.pack(pady=20)
#tree_frame.place(x=20,y=20,width=1400,height=400)
tree_scroll=Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

my_tree_1=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set)
my_tree_1.pack()

tree_scroll.config(command=my_tree_1.yview)


my_tree_1['columns'] = ("Record No","Firstname","Lastname","Home Address","Contact","Email","Role")

my_tree_1.column("#0",width=0,stretch=NO)
my_tree_1.column("Record No",anchor=W,width=150)
my_tree_1.column("Firstname",anchor=W,width=150)
my_tree_1.column("Lastname",anchor=W,width=150)
my_tree_1.column("Home Address",anchor=W,width=450)
my_tree_1.column("Contact",anchor=W,width=150)
my_tree_1.column("Email",anchor=W,width=150)
my_tree_1.column("Role",anchor=W,width=150)


my_tree_1.heading("#0",text="",anchor=W)
my_tree_1.heading("Record No",text="Record No",anchor=W)
my_tree_1.heading("Firstname",text="Firstname",anchor=W)
my_tree_1.heading("Lastname",text="Lastname",anchor=W)
my_tree_1.heading("Home Address",text="Home Address",anchor=W)
my_tree_1.heading("Contact",text="Contact",anchor=W)
my_tree_1.heading("Email",text="Email",anchor=W)
my_tree_1.heading("Role",text="Role",anchor=W)



#my_tree_1.place(x=20,y=20,width=1400,height=400)


butt=Button(tab4,text="display vm",fg="black",bg="yellow",font="bold",command=show)
butt.place(x=20,y=300,height=40,width=150)

tab4_button=Button(tab4,text="Quit prog",font="bold",command=tab4.quit)
tab4_button.place(x=20,y=350,height=40,width=150)

tab1_button=Button(tab1,text="Quit prog",font="bold",fg="blue",command=tab1.quit)
tab1_button.place(x=20,y=350,height=40,width=150)

tab2_button=Button(tab2,text="Quit prog",font="bold",fg="blue",command=tab2.quit)
tab2_button.place(x=20,y=700,height=40,width=150)

tab3_button=Button(tab3,text="Quit prog",font="bold",fg="blue",command=tab3.quit)
tab3_button.place(x=20,y=700,height=40,width=150)



#event logistics treeview display widgets and buttons

tree_frame_2=Frame(tab5)
tree_frame_2.pack(pady=20,padx=20)
#tree_frame.place(x=20,y=20,width=1400,height=400)
tree_scroll_2=Scrollbar(tree_frame_2)
tree_scroll_2.pack(side=RIGHT,fill=Y)

my_tree_2=ttk.Treeview(tree_frame_2,yscrollcommand=tree_scroll_2.set)
my_tree_2.pack()

tree_scroll_2.config(command=my_tree_2.yview)


my_tree_2['columns'] = ("Record No","Event Logistics Services","Description","Contact","Email")

my_tree_2.column("#0",width=0,stretch=NO)
my_tree_2.column("Record No",anchor=W,width=90)
my_tree_2.column("Event Logistics Services",anchor=W,width=200)
my_tree_2.column("Description",anchor=W,width=500)
my_tree_2.column("Contact",anchor=W,width=150)
my_tree_2.column("Email",anchor=W,width=120)



my_tree_2.heading("#0",text="",anchor=W)
my_tree_2.heading("Record No",text="Record No",anchor=W)
my_tree_2.heading("Event Logistics Services",text="Event Logistics Services",anchor=W)
my_tree_2.heading("Description",text="Description",anchor=W)
my_tree_2.heading("Contact",text="Contact",anchor=W)
my_tree_2.heading("Email",text="Email",anchor=W)




#my_tree_1.place(x=20,y=20,width=1400,height=400)


logbut=Button(tab5,text="display event",fg="black",bg="yellow",font="bold",command=show_1)
logbut.place(x=20,y=530,height=40,width=150)

# # taxi logistics treeview display widgets and buttons

tree_frame_3=Frame(tab5)
tree_frame_3.pack(pady=20,padx=20)
#tree_frame.place(x=20,y=20,width=1400,height=400)
tree_scroll_3=Scrollbar(tree_frame_3)
tree_scroll_3.pack(side=RIGHT,fill=Y)

my_tree_3=ttk.Treeview(tree_frame_3,yscrollcommand=tree_scroll_3.set)
my_tree_3.pack()

tree_scroll_3.config(command=my_tree_3.yview)


my_tree_3['columns'] = ("Record No","Taxi","Description","Contact","Email")

my_tree_3.column("#0",width=0,stretch=NO)
my_tree_3.column("Record No",anchor=W,width=90)
my_tree_3.column("Taxi",anchor=W,width=200)
my_tree_3.column("Description",anchor=W,width=500)
my_tree_3.column("Contact",anchor=W,width=150)
my_tree_3.column("Email",anchor=W,width=120)



my_tree_3.heading("#0",text="",anchor=W)
my_tree_3.heading("Record No",text="Record No",anchor=W)
my_tree_3.heading("Taxi",text="Taxi",anchor=W)
my_tree_3.heading("Description",text="Description",anchor=W)
my_tree_3.heading("Contact",text="Contact",anchor=W)
my_tree_3.heading("Email",text="Email",anchor=W)




#my_tree_1.place(x=20,y=20,width=1400,height=400)


logtaxi=Button(tab5,text="display Taxis",fg="black",bg="yellow",font="bold",command=show_2)
logtaxi.place(x=20,y=575,height=40,width=150)

# treview widgets for entertainment agencies


tree_frame_4=Frame(tab6)
tree_frame_4.pack(pady=20,padx=20)
#tree_frame.place(x=20,y=20,width=1400,height=400)
tree_scroll_4=Scrollbar(tree_frame_4)
tree_scroll_4.pack(side=RIGHT,fill=Y)

my_tree_4=ttk.Treeview(tree_frame_4,yscrollcommand=tree_scroll_4.set)
my_tree_4.pack()

tree_scroll_4.config(command=my_tree_4.yview)


my_tree_4['columns'] = ("Record No","Entertainment Agencies","Description","Contact","Email")

my_tree_4.column("#0",width=0,stretch=NO)
my_tree_4.column("Record No",anchor=W,width=90)
my_tree_4.column("Entertainment Agencies",anchor=W,width=200)
my_tree_4.column("Description",anchor=W,width=500)
my_tree_4.column("Contact",anchor=W,width=150)
my_tree_4.column("Email",anchor=W,width=120)



my_tree_4.heading("#0",text="",anchor=W)
my_tree_4.heading("Record No",text="Record No",anchor=W)
my_tree_4.heading("Entertainment Agencies",text="Entertainment Agencies",anchor=W)
my_tree_4.heading("Description",text="Description",anchor=W)
my_tree_4.heading("Contact",text="Contact",anchor=W)
my_tree_4.heading("Email",text="Email",anchor=W)




#my_tree_1.place(x=20,y=20,width=1400,height=400)


logtent=Button(tab6,text="display E-Agencies",fg="black",bg="yellow",font="bold",command=show_3)
logtent.place(x=20,y=550,height=40,width=230)

# treeview and widgets for staffing agencies

tree_frame_5=Frame(tab6)
tree_frame_5.pack(pady=20,padx=20)
#tree_frame.place(x=20,y=20,width=1400,height=400)
tree_scroll_5=Scrollbar(tree_frame_5)
tree_scroll_5.pack(side=RIGHT,fill=Y)

my_tree_5=ttk.Treeview(tree_frame_5,yscrollcommand=tree_scroll_5.set)
my_tree_5.pack()

tree_scroll_5.config(command=my_tree_5.yview)


my_tree_5['columns'] = ("Record No","Staffing Agencies","Description","Contact","Email")

my_tree_5.column("#0",width=0,stretch=NO)
my_tree_5.column("Record No",anchor=W,width=90)
my_tree_5.column("Staffing Agencies",anchor=W,width=200)
my_tree_5.column("Description",anchor=W,width=500)
my_tree_5.column("Contact",anchor=W,width=150)
my_tree_5.column("Email",anchor=W,width=120)



my_tree_5.heading("#0",text="",anchor=W)
my_tree_5.heading("Record No",text="Record No",anchor=W)
my_tree_5.heading("Staffing Agencies",text="Staffing Agencies",anchor=W)
my_tree_5.heading("Description",text="Description",anchor=W)
my_tree_5.heading("Contact",text="Contact",anchor=W)
my_tree_5.heading("Email",text="Email",anchor=W)




#my_tree_1.place(x=20,y=20,width=1400,height=400)


logtent=Button(tab6,text="display Staff-Agencies",fg="black",bg="yellow",font="bold",command=show_4)
logtent.place(x=20,y=595,height=40,width=230)

#treeview display widgets for hr resource security companies

tree_frame_6=Frame(tab7)
tree_frame_6.pack(pady=20,padx=20)
#tree_frame.place(x=20,y=20,width=1400,height=400)
tree_scroll_6=Scrollbar(tree_frame_6)
tree_scroll_6.pack(side=RIGHT,fill=Y)

my_tree_6=ttk.Treeview(tree_frame_6,yscrollcommand=tree_scroll_6.set)
my_tree_6.pack()

tree_scroll_6.config(command=my_tree_6.yview)


my_tree_6['columns'] = ("Record No","Security Companies","Description","Contact","Email")

my_tree_6.column("#0",width=0,stretch=NO)
my_tree_6.column("Record No",anchor=W,width=90)
my_tree_6.column("Security Companies",anchor=W,width=200)
my_tree_6.column("Description",anchor=W,width=500)
my_tree_6.column("Contact",anchor=W,width=150)
my_tree_6.column("Email",anchor=W,width=120)



my_tree_6.heading("#0",text="",anchor=W)
my_tree_6.heading("Record No",text="Record No",anchor=W)
my_tree_6.heading("Security Companies",text="Security Companies",anchor=W)
my_tree_6.heading("Description",text="Description",anchor=W)
my_tree_6.heading("Contact",text="Contact",anchor=W)
my_tree_6.heading("Email",text="Email",anchor=W)




#my_tree_1.place(x=20,y=20,width=1400,height=400)


logtsecu=Button(tab7,text="display Security Com",fg="black",bg="yellow",font="bold",command=show_5)
logtsecu.place(x=20,y=530,height=40,width=230)


#treeview display widgets for hotels

tree_frame_7=Frame(tab7)
tree_frame_7.pack(pady=20,padx=20)
#tree_frame.place(x=20,y=20,width=1400,height=400)
tree_scroll_7=Scrollbar(tree_frame_7)
tree_scroll_7.pack(side=RIGHT,fill=Y)

my_tree_7=ttk.Treeview(tree_frame_7,yscrollcommand=tree_scroll_7.set)
my_tree_7.pack()

tree_scroll_7.config(command=my_tree_7.yview)


my_tree_7['columns'] = ("Record No","Hotels","Description","Contact","Email")

my_tree_7.column("#0",width=0,stretch=NO)
my_tree_7.column("Record No",anchor=W,width=90)
my_tree_7.column("Hotels",anchor=W,width=200)
my_tree_7.column("Description",anchor=W,width=500)
my_tree_7.column("Contact",anchor=W,width=150)
my_tree_7.column("Email",anchor=W,width=120)



my_tree_7.heading("#0",text="",anchor=W)
my_tree_7.heading("Record No",text="Record No",anchor=W)
my_tree_7.heading("Hotels",text="Hotels",anchor=W)
my_tree_7.heading("Description",text="Description",anchor=W)
my_tree_7.heading("Contact",text="Contact",anchor=W)
my_tree_7.heading("Email",text="Email",anchor=W)




#my_tree_1.place(x=20,y=20,width=1400,height=400)


logthot=Button(tab7,text="display Hotels",fg="black",bg="yellow",font="bold",command=show_6)
logthot.place(x=20,y=575,height=40,width=230)


# delete labelframe for volunteer management
vm_del_label=LabelFrame(tab4,text="Delete Volunteer Record",font="bold",fg="blue" )
vm_del_label.place(x=190,y=300,height=90,width=350)
vmp_label=Label(vm_del_label,text="enter record No",fg="black",font="bold")
vmp_label.place(x=2,y=2,width=150,height=20)
vmp_entry=Entry(vm_del_label)
vmp_entry.place(x=155,y=2,width=90,height=20)
delbut=Button(vm_del_label,text="Delete",fg="black",font="bold",command=vm_del)
delbut.place(x=155,y=29,width=133,height=30)

# update labelframe for volunteer management

vm_update_label=LabelFrame(tab4,text="Update Volunteer Record",font="bold",fg="blue" )
vm_update_label.place(x=600,y=300,height=220,width=700)
rec_no=Label(vm_update_label,text="record No",fg="black",font="bold")
rec_no_entry=Entry(vm_update_label)
rec_no.place(x=1,y=1,width=120,height=20)
rec_no_entry.place(x=150,y=1,width=120,height=20)

first_no=Label(vm_update_label,text="firstname",fg="black",font="bold")
first_no_entry=Entry(vm_update_label)
first_no.place(x=1,y=23,width=120,height=20)
first_no_entry.place(x=150,y=23,width=200,height=20)

last_no=Label(vm_update_label,text="lastname",fg="black",font="bold")
last_no_entry=Entry(vm_update_label)
last_no.place(x=1,y=44,width=120,height=20)
last_no_entry.place(x=150,y=44,width=200,height=20)

hom_no=Label(vm_update_label,text="home address",fg="black",font="bold")
hom_no_entry=Entry(vm_update_label)
hom_no.place(x=1,y=66,width=150,height=20)
hom_no_entry.place(x=150,y=66,width=450,height=20)

cont_no=Label(vm_update_label,text="contact",fg="black",font="bold")
cont_no_entry=Entry(vm_update_label)
cont_no.place(x=1,y=88,width=100,height=20)
cont_no_entry.place(x=150,y=88,width=200,height=20)


mail_no=Label(vm_update_label,text="email",fg="black",font="bold")
mail_no_entry=Entry(vm_update_label)
mail_no.place(x=1,y=110,width=80,height=20)
mail_no_entry.place(x=150,y=110,width=200,height=20)

role_no=Label(vm_update_label,text="role",fg="black",font="bold")
role_no_entry=Entry(vm_update_label)
role_no.place(x=1,y=132,width=80,height=20)
role_no_entry.place(x=150,y=132,width=200,height=20)

vm_updat_but=Button(vm_update_label,text="Update",fg="black",font="bold",command=vm_updat)
vm_updat_but.place(x=150,y=158,width=100,height=30)

#delete labelframe for event logistics services

evt_del_label=LabelFrame(tab5,text="Delete Event logistics Record",font="bold",fg="blue" )
evt_del_label.place(x=190,y=530,height=90,width=350)
evt_label=Label(evt_del_label,text="enter record No",fg="black",font="bold")
evt_label.place(x=2,y=2,width=150,height=20)
evt_entry=Entry(evt_del_label)
evt_entry.place(x=155,y=2,width=90,height=20)
evt_del_but=Button(evt_del_label,text="Delete",fg="black",font="bold",command=elog_del)
evt_del_but.place(x=155,y=29,width=133,height=30)

#delete labelframe for taxi services

taxi_del_label=LabelFrame(tab5,text="Delete Taxi Records",font="bold",fg="blue" )
taxi_del_label.place(x=190,y=625,height=90,width=350)
taxi_label=Label(taxi_del_label,text="enter record No",fg="black",font="bold")
taxi_label.place(x=2,y=2,width=150,height=20)
taxi_entry=Entry(taxi_del_label)
taxi_entry.place(x=155,y=2,width=90,height=20)
taxi_del_but=Button(taxi_del_label,text="Delete",fg="black",font="bold",command=eTax_del)
taxi_del_but.place(x=155,y=29,width=133,height=30)


# quit button for logistics
lbutt=Button(tab5,text="Quit Prog",fg="black",font="bold",bg="yellow",command=tab5.quit)
lbutt.place(x=190,y=720,width=100,height=50)

# update label frame for event logistics services

log_update_label=LabelFrame(tab5,text="Update Event Logistics Record",font="bold",fg="blue" )
log_update_label.place(x=600,y=530,height=180,width=760)
evt_no=Label(log_update_label,text="record No",fg="black",font="bold")
evt_no_entry=Entry(log_update_label)
evt_no.place(x=1,y=1,width=120,height=20)
evt_no_entry.place(x=270,y=1,width=120,height=20)

elsl_no=Label(log_update_label,text="event logistics serv lond",fg="black",font="bold")
elsl_no_entry=Entry(log_update_label)
elsl_no.place(x=1,y=23,width=240,height=22)
elsl_no_entry.place(x=270,y=23,width=200,height=20)

desc_no=Label(log_update_label,text="description",fg="black",font="bold")
desc_no_entry=Entry(log_update_label)
desc_no.place(x=1,y=47,width=125,height=20)
desc_no_entry.place(x=270,y=44,width=370,height=20)


contlog_no=Label(log_update_label,text="contact",fg="black",font="bold")
contlog_no_entry=Entry(log_update_label)
contlog_no.place(x=1,y=67,width=100,height=20)
contlog_no_entry.place(x=270,y=67,width=200,height=20)


maillog_no=Label(log_update_label,text="email",fg="black",font="bold")
maillog_no_entry=Entry(log_update_label)
maillog_no.place(x=1,y=90,width=80,height=20)
maillog_no_entry.place(x=270,y=90,width=200,height=20)



log_updat_but=Button(log_update_label,text="Update",fg="black",font="bold",command=levt_updat)
log_updat_but.place(x=270,y=115,width=100,height=30)

# update label frame for taxi records

tax_update_label=LabelFrame(tab5,text="Update Taxi Record",font="bold",fg="blue" )
tax_update_label.place(x=600,y=715,height=180,width=760)
tax_no=Label(tax_update_label,text="record No",fg="black",font="bold")
tax_no_entry=Entry(tax_update_label)
tax_no.place(x=1,y=1,width=120,height=20)
tax_no_entry.place(x=270,y=1,width=120,height=20)

taxi_no=Label(tax_update_label,text="taxi",fg="black",font="bold")
taxi_no_entry=Entry(tax_update_label)
taxi_no.place(x=1,y=23,width=80,height=22)
taxi_no_entry.place(x=270,y=23,width=150,height=20)

taxii_no=Label(tax_update_label,text="description",fg="black",font="bold")
taxii_no_entry=Entry(tax_update_label)
taxii_no.place(x=1,y=47,width=125,height=20)
taxii_no_entry.place(x=270,y=44,width=370,height=20)


conttax_no=Label(tax_update_label,text="contact",fg="black",font="bold")
conttax_no_entry=Entry(tax_update_label)
conttax_no.place(x=1,y=67,width=100,height=20)
conttax_no_entry.place(x=270,y=67,width=200,height=20)


mailtax_no=Label(tax_update_label,text="email",fg="black",font="bold")
mailtax_no_entry=Entry(tax_update_label)
mailtax_no.place(x=1,y=90,width=80,height=20)
mailtax_no_entry.place(x=270,y=90,width=200,height=20)



taxi_updat_but=Button(tax_update_label,text="Update",fg="black",font="bold",command=taxxi_updat)
taxi_updat_but.place(x=270,y=115,width=100,height=30)

#delete labelframe for entertainment agencies services

ent_del_label=LabelFrame(tab6,text="Delete Entertainment agencies Record",font="bold",fg="blue" )
ent_del_label.place(x=255,y=530,height=90,width=350)
ent_label=Label(ent_del_label,text="enter record No",fg="black",font="bold")
ent_label.place(x=2,y=2,width=150,height=20)
ent_entry=Entry(ent_del_label)
ent_entry.place(x=155,y=2,width=90,height=20)
ent_del_but=Button(ent_del_label,text="Delete",fg="black",font="bold",command=eal_del)
ent_del_but.place(x=155,y=29,width=133,height=30)

#delete labelframe for event staffing services

estaff_del_label=LabelFrame(tab6,text="Delete event staffing  Records",font="bold",fg="blue" )
estaff_del_label.place(x=255,y=625,height=90,width=350)
estaff_label=Label(estaff_del_label,text="enter record No",fg="black",font="bold")
estaff_label.place(x=2,y=2,width=150,height=20)
estaff_entry=Entry(estaff_del_label)
estaff_entry.place(x=155,y=2,width=90,height=20)
estaff_del_but=Button(estaff_del_label,text="Delete",fg="black",font="bold",command=event_staff_del)
estaff_del_but.place(x=155,y=29,width=133,height=30)



# update label frame for entertainment agencies services

ent_update_label=LabelFrame(tab6,text="Update Entertainment agencies Record",font="bold",fg="blue" )
ent_update_label.place(x=650,y=530,height=180,width=760)
ent_no=Label(ent_update_label,text="record No",fg="black",font="bold")
ent_no_entry=Entry(ent_update_label)
ent_no.place(x=1,y=1,width=120,height=20)
ent_no_entry.place(x=270,y=1,width=120,height=20)

enta_no=Label(ent_update_label,text="entertainment agencies",fg="black",font="bold")
enta_no_entry=Entry(ent_update_label)
enta_no.place(x=1,y=23,width=240,height=22)
enta_no_entry.place(x=270,y=23,width=200,height=20)

descent_no=Label(ent_update_label,text="description",fg="black",font="bold")
descent_ent_entry=Entry(ent_update_label)
descent_no.place(x=1,y=47,width=125,height=20)
descent_ent_entry.place(x=270,y=44,width=370,height=20)


contlogent_no=Label(ent_update_label,text="contact",fg="black",font="bold")
contlogent_no_entry=Entry(ent_update_label)
contlogent_no.place(x=1,y=67,width=100,height=20)
contlogent_no_entry.place(x=270,y=67,width=200,height=20)


maillent_no=Label(ent_update_label,text="email",fg="black",font="bold")
maillent_no_entry=Entry(ent_update_label)
maillent_no.place(x=1,y=90,width=80,height=20)
maillent_no_entry.place(x=270,y=90,width=200,height=20)



logent_updat_but=Button(ent_update_label,text="Update",fg="black",font="bold",command=eAL_updat)
logent_updat_but.place(x=270,y=115,width=100,height=30)



# update label frame for event staffing records

staff_update_label=LabelFrame(tab6,text="Update Taxi Record",font="bold",fg="blue" )
staff_update_label.place(x=650,y=715,height=180,width=760)
staff_no=Label(staff_update_label,text="record No",fg="black",font="bold")
staff_no_entry=Entry(staff_update_label)
staff_no.place(x=1,y=1,width=120,height=20)
staff_no_entry.place(x=270,y=1,width=120,height=20)

sta_no=Label(staff_update_label,text="event staffing agencies",fg="black",font="bold")
sta_no_entry=Entry(staff_update_label)
sta_no.place(x=1,y=23,width=200,height=22)
sta_no_entry.place(x=270,y=23,width=200,height=20)

staffd_no=Label(staff_update_label,text="description",fg="black",font="bold")
staffd_no_entry=Entry(staff_update_label)
staffd_no.place(x=1,y=47,width=125,height=20)
staffd_no_entry.place(x=270,y=44,width=370,height=20)


contstaff_no=Label(staff_update_label,text="contact",fg="black",font="bold")
contstaff_no_entry=Entry(staff_update_label)
contstaff_no.place(x=1,y=67,width=100,height=20)
contstaff_no_entry.place(x=270,y=67,width=200,height=20)


mailstaff_no=Label(staff_update_label,text="email",fg="black",font="bold")
mailstaff_no_entry=Entry(staff_update_label)
mailstaff_no.place(x=1,y=90,width=80,height=20)
mailstaff_no_entry.place(x=270,y=90,width=200,height=20)



staff_updat_but=Button(staff_update_label,text="Update",fg="black",font="bold",command=etaff_updat)
staff_updat_but.place(x=270,y=115,width=100,height=30)

#quit button in tab6
quithr=Button(tab6,text="Quit prog",fg="black",bg="yellow",font="bold",command=tab6.quit)
quithr.place(x=20,y=650,width=150,height=40)

#delete labelframe for security companies

sec_del_label=LabelFrame(tab7,text="Delete Security Company Record",font="bold",fg="blue" )
sec_del_label.place(x=255,y=530,height=90,width=350)
sec_label=Label(sec_del_label,text="enter record No",fg="black",font="bold")
sec_label.place(x=2,y=2,width=150,height=20)
sec_entry=Entry(sec_del_label)
sec_entry.place(x=155,y=2,width=90,height=20)
sec_del_but=Button(sec_del_label,text="Delete",fg="black",font="bold",command=security_comp_del)
sec_del_but.place(x=155,y=29,width=133,height=30)

#delete labelframe for hotels

hot_del_label=LabelFrame(tab7,text="Delete Hotel  Records",font="bold",fg="blue" )
hot_del_label.place(x=255,y=625,height=90,width=350)
hot_label=Label(hot_del_label,text="enter record No",fg="black",font="bold")
hot_label.place(x=2,y=2,width=150,height=20)
hot_entry=Entry(hot_del_label)
hot_entry.place(x=155,y=2,width=90,height=20)
hot_del_but=Button(hot_del_label,text="Delete",fg="black",font="bold",command=hotel_comp_del)
hot_del_but.place(x=155,y=29,width=133,height=30)

sechotbutt=Button(tab7,text="Quit prog",fg="black",bg="yellow",font="bold",command=tab7.quit)
sechotbutt.place(x=20,y=620,width=150,height=50)

# update label frame for security companies

s_update_label=LabelFrame(tab7,text="Update Security Company Record",font="bold",fg="blue" )
s_update_label.place(x=650,y=530,height=180,width=760)
s_no=Label(s_update_label,text="record No",fg="black",font="bold")
s_no_entry=Entry(s_update_label)
s_no.place(x=1,y=1,width=120,height=20)
s_no_entry.place(x=270,y=1,width=120,height=20)

sn_no=Label(s_update_label,text="security company",fg="black",font="bold")
sn_no_entry=Entry(s_update_label)
sn_no.place(x=1,y=23,width=170,height=22)
sn_no_entry.place(x=270,y=23,width=200,height=20)

sndes_no=Label(s_update_label,text="description",fg="black",font="bold")
sndes_ent_entry=Entry(s_update_label)
sndes_no.place(x=1,y=47,width=125,height=20)
sndes_ent_entry.place(x=270,y=44,width=370,height=20)

sncont=Label(s_update_label,text="contact",fg="black",font="bold")
sncont_no_entry=Entry(s_update_label)
sncont.place(x=1,y=67,width=100,height=20)
sncont_no_entry.place(x=270,y=67,width=200,height=20)

maillsnc_no=Label(s_update_label,text="email",fg="black",font="bold")
maillsnc_no_entry=Entry(s_update_label)
maillsnc_no.place(x=1,y=90,width=80,height=20)
maillsnc_no_entry.place(x=270,y=90,width=200,height=20)

sc_updat_but=Button(s_update_label,text="Update",fg="black",font="bold",command=security_updat)
sc_updat_but.place(x=270,y=115,width=100,height=30)


# update label frame for Hotel records

htl_update_label=LabelFrame(tab7,text="Update Hotel Record",font="bold",fg="blue" )
htl_update_label.place(x=650,y=715,height=180,width=760)
htl_no=Label(htl_update_label,text="record No",fg="black",font="bold")
htl_no_entry=Entry(htl_update_label)
htl_no.place(x=1,y=1,width=120,height=20)
htl_no_entry.place(x=270,y=1,width=120,height=20)

htl_name=Label(htl_update_label,text="hotel",fg="black",font="bold")
htln=Entry(htl_update_label)
htl_name.place(x=1,y=23,width=120,height=22)
htln.place(x=270,y=23,width=200,height=20)

staffd_no=Label(htl_update_label,text="description",fg="black",font="bold")
staffd_no_entry=Entry(htl_update_label)
staffd_no.place(x=1,y=47,width=125,height=20)
staffd_no_entry.place(x=270,y=44,width=370,height=20)


conthtl=Label(htl_update_label,text="contact",fg="black",font="bold")
conthtlentry=Entry(htl_update_label)
conthtl.place(x=1,y=67,width=100,height=20)
conthtlentry.place(x=270,y=67,width=200,height=20)


mailhtl_no=Label(htl_update_label,text="email",fg="black",font="bold")
mailhtl_no_entry=Entry(htl_update_label)
mailhtl_no.place(x=1,y=90,width=80,height=20)
mailhtl_no_entry.place(x=270,y=90,width=200,height=20)



htl_updat_but=Button(htl_update_label,text="Update",fg="black",font="bold",command=hotely_updat)
htl_updat_but.place(x=270,y=115,width=100,height=30)




window.mainloop()