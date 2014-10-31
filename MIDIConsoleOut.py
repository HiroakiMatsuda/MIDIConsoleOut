#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-
# This module has been tested on python ver.2.6.6.
# ver0.141030
# (C) 2014 Matsuda Hiroaki

"""
 @file MIDIConsoleOut.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import MIDI

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
midiconsoleout_spec = ["implementation_id", "MIDIConsoleOut", 
		 "type_name",         "MIDIConsoleOut", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "Hiroaki Matsuda", 
		 "category",          "MIDI", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.mode", "0",
		 "conf.__widget__.mode", "text",
		 ""]
# </rtc-template>

##
# @class MIDIConsoleOut
# @brief ModuleDescription
# 
#

def print_message(message, mode):

        if mode == 1:               
                if message.event == 'Note On':
                        print("Event:%12s Ch:%2d Note:%2d Vel:%3d" %(message.event,
                                                                     message.ch.channel,
                                                                     message.ch.note_number,
                                                                     message.ch.velocity))
                elif message.event == 'Note Off':
                        print("Event:%12s Ch:%2d Note:%2d Vel:%3d" %(message.event,
                                                                     message.ch.channel,
                                                                     message.ch.note_number,
                                                                     message.ch.velocity))

        elif mode == 2:
                print("Event:%s" %(message.event))

        else:
                print("%s" %(message))

        
class DataListener(OpenRTM_aist.ConnectorDataListenerT):
        
        def __init__(self, name, mode):
                self._name = name
                self._mode = mode
                
        def __del__(self):
                print("dtor of %s" %(self._name))

        def __call__(self, info, cdrdata):
                data = OpenRTM_aist.ConnectorDataListenerT.__call__(self,
                                                                    info,
                                                                    cdrdata,
                                                                    MIDI.MIDIMessage(RTC.Time(0, 0),
                                                                                     '',
                                                                                     MIDI.ChannelMessage(0, 0, 0, 0, 0, 0, 0, 0, 0),
                                                                                     MIDI.SystemMessage("", 0,"","","","","",
                                                                                                        "","","","", 0, 0, 0,
                                                                                                         0, 0, 0, 0, 0, 0, 0)))
                
                print_message(data, self._mode)

class MIDIConsoleOut(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_message = MIDI.MIDIMessage(RTC.Time(0,0),
                                                   '',
                                                   MIDI.ChannelMessage(0, 0, 0, 0, 0, 0, 0, 0, 0),
                                                   MIDI.SystemMessage("", 0,"","","","","",
                                                                      "","","","", 0, 0, 0,
                                                                       0, 0, 0, 0, 0, 0, 0))
		"""
		"""
		self._midi_inIn = OpenRTM_aist.InPort("midi_in", self._d_message)


		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  mode
		 - DefaultValue: 0
		"""
		self._mode = [0]
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("mode", self._mode, "0")
		
		# Set InPort buffers
		self.addInPort("midi_in",self._midi_inIn)
		
		# Set OutPort buffers
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The startup action when ExecutionContext startup
		# former rtc_starting_entry()
		# 
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onStartup(self, ec_id):
                self._midi_inIn.addConnectorDataListener(OpenRTM_aist.ConnectorDataListenerType.ON_RECEIVED,
                                                         DataListener("ON_RECEIVED", self._mode[0]))
	
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The activated action (Active state entry action)
	#	# former rtc_active_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	# 
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onActivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The deactivated action (Active state exit action)
	#	# former rtc_active_exit()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The execution action that is invoked periodically
	#	# former rtc_active_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onExecute(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def MIDIConsoleOutInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=midiconsoleout_spec)
    manager.registerFactory(profile,
                            MIDIConsoleOut,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    MIDIConsoleOutInit(manager)

    # Create a component
    comp = manager.createComponent("MIDIConsoleOut")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

