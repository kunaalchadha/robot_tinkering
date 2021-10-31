# Robot-Tinkering
Opensource workflows to communicate with KUKA (KRC2/4) and Universal Robots in realtime through grasshopper. The workflows have been tested and developed at Institute of Advanced Architecture for Catalonia (IAAC) in Barcelona.




****KUKA robots using KUKAVARPROXY****
This workflow has been integrated into the grasshopper environment based on the precedent work done by ([https://github.com/ImtsSrl/KUKAVARPROXY] (url)). It works on accessing global variables on the KRC side using KUKAVARPROXY as a bridge over TCP/IP. This workflow has been tested on KRC2 and KRC4 controllers.


![KVP](https://user-images.githubusercontent.com/88770685/139601624-f89cd466-8c97-4b0b-96c5-f3cfe531f779.jpg)



****Universal Robots using****
The following is a rework on the example file provided by Universal Robots for E series using Real-Time Data Exchange (RTDE) library([https://www.universal-robots.com/articles/ur/interface-communication/real-time-data-exchange-rtde-guide/](url))

![ur](https://user-images.githubusercontent.com/88770685/139601723-6973ff63-8250-4a48-887d-d6c1c375e161.jpg)

