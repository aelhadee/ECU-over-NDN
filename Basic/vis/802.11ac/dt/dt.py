import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 14})

# df = pd.read_csv('Untitled 1.csv')
df= pd.read_csv('dt.csv')
# df1 = pd.read_csv('rx_sec_dds_vs_ndn_11-11.csv')
# ax = df.plot(kind='box', title='DDS vs NDN')
#
# plt.show()
# ax = df.plot(kind='line', title='DDS vs NDN')
# plt.show()
# df[['rx_dds_cam', 'rx_ndn_cam']].plot(kind='line', )
# plt.show()
#
# df1.plot(kind='box')showfliers=False
# Line2D.zorder = 5
df1 =df[['lidar_ndn_tcp_b','lidar_ndn_udp_b',
         'lidar_ndn_tcp_s', 'lidar_ndn_udp_s',
         'lidar_dds']]
print(df1.describe(), 'lidars')
df2 =df[['can_ndn_tcp_b','can_ndn_udp_b',
         'can_ndn_tcp_s','can_ndn_udp_s'
        ,'can_dds']]
print(df2.describe(), 'CAN')

df3 =df[['cam_ndn_tcp_b', 'cam_ndn_udp_b',
         'cam_ndn_tcp_s','cam_ndn_udp_s',
         'cam_dds']]
print(df3.describe(), 'cam')
flierprops = dict(marker='x', markerfacecolor='b', markersize=4,
                  linestyle='none')
df1 =df1.boxplot(widths = 0.7, showfliers = True, flierprops=flierprops,
                                                                      whiskerprops = dict(linestyle='-',linewidth=2.0, color='black'),
                                                                      boxprops= dict(linewidth=2.0, color='black',))

plt.title( 'Received Lidar packets - RPi 1')
plt.ylabel ('Time (Milliseconds)')
#                )))
plt.xticks([1,2, 3, 4, 5],['NDN TCP (B)', 'NDN UDP (B)',
                           'NDN TCP (S)','NDN UDP (S)' ,
                           'DDS RTPS'])
# plt.boxplot(df1)
plt.axhline(y=5, color='r', linestyle='--')

plt.show()
df2 =df2.boxplot(widths = 0.7, showfliers = True, flierprops=flierprops,
                                                                      whiskerprops = dict(linestyle='-',linewidth=2.0, color='black'),
                                                                      boxprops= dict(linewidth=2.0, color='black',))

plt.title( 'Received CAN packets - RPi 2')
plt.ylabel ('Time (Milliseconds)')
#                )))
plt.xticks([1,2,3, 4, 5],['NDN TCP (B)','NDN UDP (B)' ,
                    'NDN TCP (S)','NDN UDP (S)' ,
                    'DDS RTPS'])
plt.axhline(y=8, color='r', linestyle='--')

plt.show()
df3 =df3.boxplot(widths = 0.7, showfliers = True, flierprops=flierprops,
                                                                      whiskerprops = dict(linestyle='-',linewidth=2.0, color='black'),
                                                                      boxprops= dict(linewidth=2.0, color='black',))

plt.title( 'Received cam packets - RPi 3')
plt.ylabel ('Time (Milliseconds)')
#                )))
plt.xticks([1,2, 3, 4, 5],['NDN TCP (B)','NDN UDP (B)',
                     'NDN TCP (S)','NDN UDP (S)',
                     'DDS RTPS'])
plt.axhline(y=20, color='r', linestyle='--')

plt.show()