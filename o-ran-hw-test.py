import sys, os, warnings
#warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager
from lxml import etree
import string
import xmltodict

def demo(host, port, user, password):
   with manager.connect(host=host, port=port, username=user, hostkey_verify=False, password=password) as m:
       #m.edit_config(target='running', config=xml_1)
       xml_data = open("../Yang_xml/hardware.xml").read()
       u1 =f'''
                <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                {xml_data}
                </config>
        '''
       data = m.edit_config(target='running', config=u1, default_operation='replace')
       print(data)

       ru_module = '''
       <hardware xmlns="urn:ietf:params:xml:ns:yang:ietf-hardware">
           <component>
               <name>ru-module</name>
           </component>
       </hardware>
       '''
       ru_port0 = '''
       <hardware xmlns="urn:ietf:params:xml:ns:yang:ietf-hardware">
           <component>
               <name>ru-port0</name>
           </component>
       </hardware>
       '''
       ru_port1 = '''
       <hardware xmlns="urn:ietf:params:xml:ns:yang:ietf-hardware">
           <component>
               <name>ru-port1</name>
           </component>
       </hardware>
       '''
       com = '''
       <hardware xmlns="urn:ietf:params:xml:ns:yang:ietf-hardware">
       </hardware>
       '''
       try:
           value_module = m.get(('subtree', ru_module)).data_xml
           #print(value_module)
       except:
           print("Can't find the ru-module")

       try:
           value_port0 = m.get(('subtree', ru_port0)).data_xml
       except:
           print("can't find the ru-port0")

       try:
           value_port1 = m.get(('subtree', ru_port1)).data_xml
       except:
           print("can't find the ru-port1")

       try:
           value_com = m.get(('subtree', com)).data_xml
           #print(value_com)
       except:
           print("can't find the hardware module")

       #xml_doc = xml.dom.minidom.parseString(value).toprettyxml()
       dict_module = xmltodict.parse(str(value_module))
       #print('dict_module :',dict_module)
       dict_port0 = xmltodict.parse(str(value_port0))
       #print('Port0 :', dict_port0)
       dict_port1 = xmltodict.parse(str(value_port1))
       #print(dict_port1)
       dict_com = xmltodict.parse(str(value_com))

       print("\n\n******validation for ru-module******\n\n")
       try:
           Class = dict_module['data']['hardware']['component']['class']['#text']
           if Class:
               print("class belongs to %s" %Class)
       except:
           print('You have to configure usermgmt yang module for class')

       try:
           oper_state = dict_module['data']['hardware']['component']['state']['oper-state']
           if oper_state:
               print("oper-state was %s" %oper_state)
       except:
           print('You have to configure usermgmt yang module for oper-state')
      
       try:
           availability_state = dict_module['data']['hardware']['component']['state']['availability-state']
           if availability_state:
               print("availability-state was %s" %availability_state)
       except:
           print('You have to configure usermgmt yang module for availability-state')

       try:
           o_ran_name = dict_module['data']['hardware']['component']['o-ran-name']['#text']
           if o_ran_name:
               print("o-ran-name was %s" %o_ran_name)
       except:
           print('You have to configure usermgmt yang module for o-ran-name')


       try:
           description = dict_module['data']['hardware']['component']['description']
           if description:
               print("description was given as %s"%description)
       except:
           print('You have to configure usermgmt yang module for description')

       try:
           hw_rev = dict_module['data']['hardware']['component']['hardware-rev']
           #print(hw_rev)
       
           if not hw_rev:
               print("hardware-rev was given as %s" %hw_rev)
       except:
           print('You have to configure usermgmt yang module for hardware-rev')
           
      
       try:
           sw_rev = dict_module['data']['hardware']['component']['software-rev']
           #print(sw_rev)
       
           if not sw_rev:
               print("software-rev was given as %s" %sw_rev)
       except:
           print('You have to configure usermgmt yang module for software-rev')
           


       try:
           sl_no = dict_module['data']['hardware']['component']['serial-num']
           #print(sl_no)
       
           if not sl_no:
               print("serial-num was given as %s" %sl_no)
       except:
           print('You have to configure usermgmt yang module for serial-num')
           

       try:
           mfg_name = dict_module['data']['hardware']['component']['mfg-name']
           #print(mfg_name)
           if not mfg_name:
               print("mfg-name was given as %s" %mfg_name)
       except:
           print('You have to configure usermgmt yang module for mfg-name')
           

       try:
           model_name = dict_module['data']['hardware']['component']['model-name']
           if model_name :
               print("model-name was given as %s" %model_name)
       except:
           print('You have to configure usermgmt yang module for model-name')

       try:
           uuid = dict_module['data']['hardware']['component']['uuid']
           if uuid :
               print("uuid is %s" %uuid)
       except:
           print('You have to configure usermgmt yang module for uuid')

       try:
           contains_child = dict_module['data']['hardware']['component']['contains-child']
           if contains_child :
               print("contains-child was given as %s" %contains_child)
       except:
           print('You have to configure usermgmt yang module for contains-child')
       try:
           product_code = dict_module['data']['hardware']['component']['product-code']['#text']
           if product_code :
               print("product-code was given as %s" %product_code)
       except:
           print('You have to configure usermgmt yang module for product-code')

       print("\n\n******validation failed for ru-port0******\n\n")

       try:
           Class1 = dict_port0['data']['hardware']['component']['class']['#text']
           if Class1 :
               print("class belongs to %s" %Class1)
       except:
           print('You have to configure usermgmt yang module for class')

       try:
           parent1 = dict_port0['data']['hardware']['component']['parent']
           if parent1:
               print("parent was given as %s" %parent1)
       except:
           print('You have to configure usermgmt yang module for parent')

       try:
           parent_rel1 = dict_port0['data']['hardware']['component']['parent-rel-pos']
           if parent_rel1:
               print("parent-rel-pos was given as %s" %parent_rel1)
       except:
           print('You have to configure usermgmt yang module for parent-rel-pos')

       try:
           oper_state1 = dict_port0['data']['hardware']['component']['state']['oper-state']
           if oper_state1:
               print("oper-state was given as %s" %oper_state1)
       except:
           print('You have to configure usermgmt yang module for oper-state')

       try:
           avail_state1 = dict_port0['data']['hardware']['component']['state']['availability-state']['#text']
           if avail_state1:
               print("availability-state was given as %s" %avail_state1)
       except:
           print('You have to configure usermgmt yang module for availability-state')

       try:
           o_ran_name1 = dict_port0['data']['hardware']['component']['o-ran-name']['#text']
           if o_ran_name1:
               print("o-ran-name was given as %s" %o_ran_name1)
       except:
           print('You have to configure usermgmt yang module for o-ran-name')

       try:
           descrip1 = dict_port0['data']['hardware']['component']['description']
           if descrip1:
               print("Description was given as %s" %descrip1)
       except:
           print('You have to configure usermgmt yang module for description')

       try:
           hw_rev1 = dict_port0['data']['hardware']['component']['hardware-rev']
           if hw_rev1:
               print("hardware-rev was given as %s" %hw_rev1)
       except:
           print('You have to configure usermgmt yang module for hardware-rev')

       try:
           is_fru1 = dict_port0['data']['hardware']['component']['is-fru']
           if is_fru1:
               print("is_fru given as %s" %is_fru1)
       except:
           print('You have to configure usermgmt yang module for is-fru')

       try:
           mfg_date1 = dict_port0['data']['hardware']['component']['mfg-date']
           if mfg_date1:
               print("mfg-date was given as %s" %mfg_date1)
       except:
           print('You have to configure usermgmt yang module for mfg-date')
      
       print("\n\n******validation for ru-port1******\n\n")

       try:
           Class2 = dict_port1['data']['hardware']['component']['class']['#text']
           if Class2:
               print("class belongs to %s" %Class2)
       except:
           print('You have to configure usermgmt yang module for class')

       try:
           parent2 = dict_port1['data']['hardware']['component']['parent']
           if parent2:
               print("parent was given as %s" %parent2)
       except:
           print('You have to configure usermgmt yang module for parent')

       try:
           parent_rel2 = dict_port1['data']['hardware']['component']['parent-rel-pos']
           if parent_rel2:
               print("parent-rel-pos was given as %s" %parent_rel2)
       except:
           print('You have to configure usermgmt yang module for parent-rel-pos')

       try:
           oper_state2 = dict_port1['data']['hardware']['component']['state']['oper-state']
           if oper_state2:
               print("oper-state was given as %s" %oper_state2)
       except:
           print('You have to configure usermgmt yang module for oper-state')

       try:
           avail_state2 = dict_port1['data']['hardware']['component']['state']['availability-state']['#text']
           if avail_state2:
               print("availability-state was given as %s" %avail_state2)
       except:
           print('You have to configure usermgmt yang module for availability-state')

       try:
           o_ran_name2 = dict_port1['data']['hardware']['component']['o-ran-name']['#text']
           if o_ran_name2:
               print("o-ran-name was given as %s" %o_ran_name2)
       except:
           print('You have to configure usermgmt yang module for o-ran-name')

       try:
           descrip2 = dict_port1['data']['hardware']['component']['description']
           if descrip2:
               print("Description was given as %s" %descrip2)
       except:
           print('You have to configure usermgmt yang module for description')

       try:
           hw_rev2 = dict_port1['data']['hardware']['component']['hardware-rev']
           if hw_rev2:
               print("hardware-rev was given as %s" %hw_rev2)
       except:
           print('You have to configure usermgmt yang module for hardware-rev')

       try:
           is_fru2 = dict_port1['data']['hardware']['component']['is-fru']
           if is_fru2:
               print("is_fru given as %s" %is_fru2)
       except:
           print('You have to configure usermgmt yang module for is-fru')

       try:
           mfg_date2 = dict_port1['data']['hardware']['component']['mfg-date']
           if mfg_date2:
               print("mfg-date was given as %s" %mfg_date2)
       except:
           print('You have to configure usermgmt yang module for mfg-date')

       try:
           last_chg = dict_com['data']['hardware']['last-change']
           if last_chg:
               print("\n\n*****last change is on %s*****\n\n"%last_chg)
       except:
           print('You have to configure usermgmt yang module for last-change')
      

      
if __name__ == '__main__':
   #give the input configuration in xml file format
   #xml_1 = open('o-ran-hardware.xml').read()
   #give the input in the format hostname, port, username, password
   demo("192.168.1.10", 830, "root", "root")

