import sys, os, warnings
#warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager, operations
import string
import xmltodict
#xml_1 = open('o-ran-interfaces.xml').read()
def demo(host, port, user, password):
    with manager.connect(host=host, port=port, username=user, hostkey_verify=False, password=password) as m:
        xml_data = open('../Yang_xml/interface.xml').read()
        u1 =f'''
                <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                {xml_data}
                </config>
        '''


        Data = m.edit_config(u1, target='running')
        print(Data)


        v_name1 = '''
                <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                    <interface>
                        <name></name>
                    </interface>
                </interfaces>
                </filter>
        '''

        
        interface_name = m.get_config('running', v_name1).data_xml
        dict_interface = xmltodict.parse(str(interface_name))
        Interfaces = dict_interface['data']['interfaces']['interface']


        interface = '''
       <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
       </interfaces>
       '''

        eth0 = f'''
       <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>{Interfaces[1]['name']}</name>
            </interface>
       </interfaces>
       '''

        eth1 = f'''
       <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>{Interfaces[2]['name']}</name>
            </interface>
       </interfaces>
       '''

        vlan1 = f'''
       <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>{Interfaces[3]['name']}</name>
            </interface>
       </interfaces>
       '''

        vlan2 = f'''
       <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>{Interfaces[4]['name']}</name>
            </interface>
       </interfaces>
       '''

        
        try:
            value_interface = m.get(('subtree', interface)).data_xml
        except:
            print("Can't find the interface")

        try:
            value_eth0 = m.get(('subtree', eth0)).data_xml
        except:
            print("Can't find the eth0")

        try:
            value_eth1 = m.get(('subtree', eth1)).data_xml
        except:
            print("Can't find the eth1")

        try:
            value_vlan1 = m.get(('subtree', vlan1)).data_xml
        except:
            print("Can't find the eth0_100")

        try:
            value_vlan2 = m.get(('subtree', vlan2)).data_xml
        except:
            print("Can't find the eth0_120")

        dict_interface = xmltodict.parse(str(value_interface))

        dict_eth0 = xmltodict.parse(str(value_eth0))
        # print(dict_eth01

        dict_eth1 = xmltodict.parse(str(value_eth1))

        dict_vlan1 = xmltodict.parse(str(value_vlan1))

        dict_vlan2 = xmltodict.parse(str(value_vlan2))

        print("\n\n******validation for eth0******\n\n")

        try:
            Enabled = dict_eth0['data']['interfaces']['interface']['ipv4']['enabled']
            if Enabled:
                print("enabled = %s" % Enabled)
        except:
            print('enabled not found')
            
        
        try:
            Forwrd = dict_eth0['data']['interfaces']['interface']['ipv4']['forwarding']
            if Forwrd:
                print("forwarding = %s" % Forwrd)
        except:
            print('forwarding not found')

        try:
            IP_ADD = dict_eth0['data']['interfaces']['interface']['ipv4']['address']['ip']
            if IP_ADD:
                print("ip = %s" % IP_ADD)
        except:
            print('ip not found')

        try:
            Netmask = dict_eth0['data']['interfaces']['interface']['ipv4']['address']['netmask']
            if Netmask:
                print("netmask = %s" % Netmask)
        except:
            print('netmask not found')

        try:
            l2_mtu = dict_eth0['data']['interfaces']['interface']['l2-mtu']['#text']
            if l2_mtu:
                print("l2_mtu = %s" % l2_mtu)
        except:
            print('l2_mtu not found')

        try:
            Vlan_tagging = dict_eth0['data']['interfaces']['interface']['vlan-tagging']['#text']
            if  Vlan_tagging:
                print("Vlan_tagging = %s" % Vlan_tagging)
        except:
            print('vlan-tagging not found')

        try:
            U_Plane_Marking = dict_eth0['data']['interfaces']['interface']['class-of-service']['u-plane-marking']
            if  U_Plane_Marking:
                print("U_Plane_Marking = %s" % U_Plane_Marking)
        except:
            print('u-plane-marking not found')

        try:
            m_Plane_Marking = dict_eth0['data']['interfaces']['interface']['class-of-service']['m-plane-marking']
            if  m_Plane_Marking:
                print("m_Plane_Marking = %s" % m_Plane_Marking)
        except:
            print('m-plane-marking not found')

        try:
            c_Plane_Marking = dict_eth0['data']['interfaces']['interface']['class-of-service']['c-plane-marking']
            if  c_Plane_Marking:
                print("c_Plane_Marking = %s" % c_Plane_Marking)
        except:
            print('c-plane-marking not found')

        try:
            s_Plane_Marking = dict_eth0['data']['interfaces']['interface']['class-of-service']['s-plane-marking']
            if  s_Plane_Marking:
                print("s_Plane_Marking = %s" % s_Plane_Marking)
        except:
            print('s-plane-marking not found')

        try:
            other_Marking = dict_eth0['data']['interfaces']['interface']['class-of-service']['other-marking']
            if other_Marking:
                print("other_Marking = %s" % other_Marking)
        except:
            print('other-marking not found')

        try:
            Mac_Address = dict_eth0['data']['interfaces']['interface']['mac-address']['#text']
            if Mac_Address:
                print("Mac_Address = %s" % Mac_Address)
        except:
            print('Mac_address not found')

        try:
            Port_Name = dict_eth0['data']['interfaces']['interface']['port-reference']['port-name']
            if Port_Name:
                print("Port_Name = %s" % Port_Name)
        except:
            print('port-name not found')

        try:
            Port_Number = dict_eth0['data']['interfaces']['interface']['port-reference']['port-number']
            if Port_Number:
                print("Port_Number = %s" % Port_Number)
        except:
            print('port-number not found')

        try:
            Last_Cleared = dict_eth0['data']['interfaces']['interface']['last-cleared']['#text']
            if Last_Cleared:
                print("Last_Cleared = %s" % Last_Cleared)
        except:
            print('Last_Cleared not found')

        try:
            Oper_S = dict_eth0['data']['interfaces']['interface']['oper-status']
            if Oper_S:
                print("oper-status = %s" % Oper_S)
        except:
            print('oper-status not found')

        try:
            PHY_ADD = dict_eth0['data']['interfaces']['interface']['phys-address']
            if PHY_ADD:
                print("phys-address = %s" % PHY_ADD)
        except:
            print('phys-address not found')
        
        try:
            Speed = dict_eth0['data']['interfaces']['interface']['speed']
            if Speed:
                print("speed = %s" % Speed)
        except:
            print('speed not found')


        print("\n\n******validation for eth1******\n\n")

        try:
            Enabled = dict_eth1['data']['interfaces']['interface']['ipv4']['enabled']
            if Enabled:
                print("enabled = %s" % Enabled)
        except:
            print('enabled not found')
            
        
        try:
            Forwrd = dict_eth1['data']['interfaces']['interface']['ipv4']['forwarding']
            if Forwrd:
                print("forwarding = %s" % Forwrd)
        except:
            print('forwarding not found')

        try:
            IP_ADD = dict_eth1['data']['interfaces']['interface']['ipv4']['address']['ip']
            if IP_ADD:
                print("ip = %s" % IP_ADD)
        except:
            print('ip not found')

        try:
            Netmask = dict_eth1['data']['interfaces']['interface']['ipv4']['address']['netmask']
            if Netmask:
                print("netmask = %s" % Netmask)
        except:
            print('netmask not found')

        try:
            l2_mtu = dict_eth1['data']['interfaces']['interface']['l2-mtu']['#text']
            if l2_mtu:
                print("l2_mtu = %s" % l2_mtu)
        except:
            print('l2_mtu not found')

        try:
            Vlan_tagging = dict_eth1['data']['interfaces']['interface']['vlan-tagging']
            if  Vlan_tagging:
                print("Vlan_tagging = %s" % Vlan_tagging)
        except:
            print('Vlan_tagging not found')

        try:
            U_Plane_Marking = dict_eth1['data']['interfaces']['interface']['class-of-service']['u-plane-marking']
            if  U_Plane_Marking:
                print("U_Plane_Marking = %s" % U_Plane_Marking)
        except:
            print('u-plane-marking not found')

        try:
            m_Plane_Marking = dict_eth1['data']['interfaces']['interface']['class-of-service']['m-plane-marking']
            if  m_Plane_Marking:
                print("m_Plane_Marking = %s" % m_Plane_Marking)
        except:
            print('m-plane-marking not found')

        try:
            c_Plane_Marking = dict_eth1['data']['interfaces']['interface']['class-of-service']['c-plane-marking']
            if  c_Plane_Marking:
                print("c_Plane_Marking = %s" % c_Plane_Marking)
        except:
            print('c-plane-marking not found')

        try:
            s_Plane_Marking = dict_eth1['data']['interfaces']['interface']['class-of-service']['s-plane-marking']
            if  s_Plane_Marking:
                print("s_Plane_Marking = %s" % s_Plane_Marking)
        except:
            print('s-plane-marking not found')

        try:
            other_Marking = dict_eth1['data']['interfaces']['interface']['class-of-service']['other-marking']
            if other_Marking:
                print("other_Marking = %s" % other_Marking)
        except:
            print('other-marking not found')

        try:
            Mac_Address = dict_eth1['data']['interfaces']['interface']['mac-address']['#text']
            if Mac_Address:
                print("Mac_Address = %s" % Mac_Address)
        except:
            print('Mac_Address not found')

        try:
            Port_Name = dict_eth1['data']['interfaces']['interface']['port-reference']['port-name']
            if Port_Name:
                print("Port_Name = %s" % Port_Name)
        except:
            print(' port-name not found')

        try:
            Port_Number = dict_eth1['data']['interfaces']['interface']['port-reference']['port-number']
            if Port_Number:
                print("Port_Number = %s" % Port_Number)
        except:
            print('port-number not found')

        try:
            Last_Cleared = dict_eth1['data']['interfaces']['interface']['last-cleared']['#text']
            if Last_Cleared:
                print("Last_Cleared = %s" % Last_Cleared)
        except:
            print('Last_Cleared not found')

        try:
            Oper_S = dict_eth1['data']['interfaces']['interface']['oper-status']
            if Oper_S:
                print("oper-status = %s" % Oper_S)
        except:
            print('oper-status not found')

        try:
            PHY_ADD = dict_eth1['data']['interfaces']['interface']['phys-address']
            if PHY_ADD:
                print("phys-address = %s" % PHY_ADD)
        except:
            print('phys-address not found')
        
        try:
            Speed = dict_eth1['data']['interfaces']['interface']['speed']
            if Speed:
                print("speed = %s" % Speed)
        except:
            print('speed not found')


        print("\n\n******validation for Vlan1******\n\n")

        try:
            Enabled = dict_vlan1['data']['interfaces']['interface']['ipv4']['enabled']
            if Enabled:
                print("enabled = %s" % Enabled)
        except:
            print('enabled not found')
            
        
        try:
            Forwrd = dict_vlan1['data']['interfaces']['interface']['ipv4']['forwarding']
            if Forwrd:
                print("forwarding = %s" % Forwrd)
        except:
            print('forwarding not found')

        try:
            IP_ADD = dict_vlan1['data']['interfaces']['interface']['ipv4']['address']['ip']
            if IP_ADD:
                print("ip = %s" % IP_ADD)
        except:
            print('ip not found')

        try:
            Netmask = dict_vlan1['data']['interfaces']['interface']['ipv4']['address']['netmask']
            if Netmask:
                print("netmask = %s" % Netmask)
        except:
            print('netmask not found')

        try:
            l2_mtu = dict_vlan1['data']['interfaces']['interface']['l2-mtu']['#text']
            if l2_mtu:
                print("l2_mtu = %s" % l2_mtu)
        except:
            print('l2_mtu not found')

        try:
            Vlan_tagging = dict_vlan1['data']['interfaces']['interface']['vlan-tagging']
            if  Vlan_tagging:
                print("Vlan_tagging = %s" % Vlan_tagging)
        except:
            print('Vlan_tagging not found')

        try:
            U_Plane_Marking = dict_vlan1['data']['interfaces']['interface']['class-of-service']['u-plane-marking']
            if  U_Plane_Marking:
                print("U_Plane_Marking = %s" % U_Plane_Marking)
        except:
            print('u-plane-marking not found')

        try:
            m_Plane_Marking = dict_vlan1['data']['interfaces']['interface']['class-of-service']['m-plane-marking']
            if  m_Plane_Marking:
                print("m_Plane_Marking = %s" % m_Plane_Marking)
        except:
            print('m-plane-marking not found')

        try:
            c_Plane_Marking = dict_vlan1['data']['interfaces']['interface']['class-of-service']['c-plane-marking']
            if  c_Plane_Marking:
                print("c_Plane_Marking = %s" % c_Plane_Marking)
        except:
            print('c-plane-marking not found')

        try:
            s_Plane_Marking = dict_vlan1['data']['interfaces']['interface']['class-of-service']['s-plane-marking']
            if  s_Plane_Marking:
                print("s_Plane_Marking = %s" % s_Plane_Marking)
        except:
            print('s-plane-marking not found')

        try:
            other_Marking = dict_vlan1['data']['interfaces']['interface']['class-of-service']['other-marking']
            if other_Marking:
                print("other_Marking = %s" % other_Marking)
        except:
            print('other-marking not found')

        try:
            Mac_Address = dict_vlan1['data']['interfaces']['interface']['mac-address']['#text']
            if Mac_Address:
                print("Mac_Address = %s" % Mac_Address)
        except:
            print('Mac_Address not found')

        try:
            Port_Name = dict_vlan1['data']['interfaces']['interface']['port-reference']['port-name']
            if Port_Name:
                print("Port_Name = %s" % Port_Name)
        except:
            print('port-name not found')

        try:
            Port_Number = dict_vlan1['data']['interfaces']['interface']['port-reference']['port-number']
            if Port_Number:
                print("Port_Number = %s" % Port_Number)
        except:
            print('port-number not found')

        try:
            Last_Cleared = dict_vlan1['data']['interfaces']['interface']['last-cleared']['#text']
            if Last_Cleared:
                print("Last_Cleared = %s" % Last_Cleared)
        except:
            print('Last_Cleared not found')

        try:
            Oper_S = dict_vlan1['data']['interfaces']['interface']['oper-status']
            if Oper_S:
                print("oper-status = %s" % Oper_S)
        except:
            print('oper-status not found')

        try:
            PHY_ADD = dict_vlan1['data']['interfaces']['interface']['phys-address']
            if PHY_ADD:
                print("phys-address = %s" % PHY_ADD)
        except:
            print('phys-address not found')
        
        try:
            Speed = dict_vlan1['data']['interfaces']['interface']['speed']
            if Speed:
                print("speed = %s" % Speed)
        except:
            print('speed not found')


        print("\n\n******validation for Vlan2******\n\n")

        try:
            Enabled = dict_vlan2['data']['interfaces']['interface']['ipv4']['enabled']
            if Enabled:
                print("enabled = %s" % Enabled)
        except:
            print('enabled not found')
            
        
        try:
            Forwrd = dict_vlan2['data']['interfaces']['interface']['ipv4']['forwarding']
            if Forwrd:
                print("forwarding = %s" % Forwrd)
        except:
            print('forwarding not found')

        try:
            IP_ADD = dict_vlan2['data']['interfaces']['interface']['ipv4']['address']['ip']
            if IP_ADD:
                print("ip = %s" % IP_ADD)
        except:
            print('ip not found')

        try:
            Netmask = dict_vlan2['data']['interfaces']['interface']['ipv4']['address']['netmask']
            if Netmask:
                print("netmask = %s" % Netmask)
        except:
            print('netmask not found')

        try:
            l2_mtu = dict_vlan2['data']['interfaces']['interface']['l2-mtu']['#text']
            if l2_mtu:
                print("l2_mtu = %s" % l2_mtu)
        except:
            print('l2_mtu not found')

        try:
            Vlan_tagging = dict_vlan2['data']['interfaces']['interface']['vlan-tagging']
            if  Vlan_tagging:
                print("Vlan_tagging = %s" % Vlan_tagging)
        except:
            print('Vlan_tagging not found')

        try:
            U_Plane_Marking = dict_vlan2['data']['interfaces']['interface']['class-of-service']['u-plane-marking']
            if  U_Plane_Marking:
                print("U_Plane_Marking = %s" % U_Plane_Marking)
        except:
            print('u-plane-marking not found')

        try:
            m_Plane_Marking = dict_vlan2['data']['interfaces']['interface']['class-of-service']['m-plane-marking']
            if  m_Plane_Marking:
                print("m_Plane_Marking = %s" % m_Plane_Marking)
        except:
            print('m-plane-marking not found')

        try:
            c_Plane_Marking = dict_vlan2['data']['interfaces']['interface']['class-of-service']['c-plane-marking']
            if  c_Plane_Marking:
                print("c_Plane_Marking = %s" % c_Plane_Marking)
        except:
            print('c-plane-marking not found')

        try:
            s_Plane_Marking = dict_vlan2['data']['interfaces']['interface']['class-of-service']['s-plane-marking']
            if  s_Plane_Marking:
                print("s_Plane_Marking = %s" % s_Plane_Marking)
        except:
            print('s-plane-marking not found')

        try:
            other_Marking = dict_vlan2['data']['interfaces']['interface']['class-of-service']['other-marking']
            if other_Marking:
                print("other_Marking = %s" % other_Marking)
        except:
            print('other-marking not found')

        try:
            Mac_Address = dict_vlan2['data']['interfaces']['interface']['mac-address']['#text']
            if Mac_Address:
                print("Mac_Address = %s" % Mac_Address)
        except:
            print('Mac_Address not found')

        try:
            Port_Name = dict_vlan2['data']['interfaces']['interface']['port-reference']['port-name']
            if Port_Name:
                print("Port_Name = %s" % Port_Name)
        except:
            print('port-name not found')

        try:
            Port_Number = dict_vlan2['data']['interfaces']['interface']['port-reference']['port-number']
            if Port_Number:
                print("Port_Number = %s" % Port_Number)
        except:
            print('port-number not found')

        try:
            Last_Cleared = dict_vlan2['data']['interfaces']['interface']['last-cleared']['#text']
            if Last_Cleared:
                print("Last_Cleared = %s" % Last_Cleared)
        except:
            print('Last_Cleared not found')

        try:
            Oper_S = dict_vlan2['data']['interfaces']['interface']['oper-status']
            if Oper_S:
                print("oper-status = %s" % Oper_S)
        except:
            print('oper-status not found')

        try:
            PHY_ADD = dict_vlan2['data']['interfaces']['interface']['phys-address']
            if PHY_ADD:
                print("phys-address = %s" % PHY_ADD)
        except:
            print('phys-address not found')
        
        try:
            Speed = dict_vlan2['data']['interfaces']['interface']['speed']
            if Speed:
                print("speed = %s" % Speed)
        except:
            print('speed not found')


        

if __name__ == '__main__':
    #give the input configuration in xml file format
    #xml_1 = open('o-ran-hardware.xml').read()
    #give the input in the format hostname, port, username, password
    # xml_data = input("Enter the xml below:\n")
    # oper=input("Enter the operation: \n")
    demo("192.168.1.10", 830, "root", "root")