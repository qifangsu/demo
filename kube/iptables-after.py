Chain PREROUTING (policy ACCEPT)
target     prot opt source               destination         
KUBE-SERVICES  all  --  0.0.0.0/0            0.0.0.0/0            /* kubernetes service portals */
DOCKER     all  --  0.0.0.0/0            0.0.0.0/0            ADDRTYPE match dst-type LOCAL

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
KUBE-SERVICES  all  --  0.0.0.0/0            0.0.0.0/0            /* kubernetes service portals */
DOCKER     all  --  0.0.0.0/0           !127.0.0.0/8          ADDRTYPE match dst-type LOCAL

Chain POSTROUTING (policy ACCEPT)
target     prot opt source               destination         
KUBE-POSTROUTING  all  --  0.0.0.0/0            0.0.0.0/0            /* kubernetes postrouting rules */
MASQUERADE  all  --  172.17.0.0/16        0.0.0.0/0           
RETURN     all  --  10.244.0.0/16        10.244.0.0/16       
MASQUERADE  all  --  10.244.0.0/16       !224.0.0.0/4         
RETURN     all  -- !10.244.0.0/16        10.244.0.0/24       
MASQUERADE  all  -- !10.244.0.0/16        10.244.0.0/16       

Chain DOCKER (2 references)
target     prot opt source               destination         
RETURN     all  --  0.0.0.0/0            0.0.0.0/0           

Chain KUBE-MARK-DROP (0 references)
target     prot opt source               destination         
MARK       all  --  0.0.0.0/0            0.0.0.0/0            MARK or 0x8000

Chain KUBE-MARK-MASQ (11 references)
target     prot opt source               destination         
MARK       all  --  0.0.0.0/0            0.0.0.0/0            MARK or 0x4000

Chain KUBE-NODEPORTS (1 references)
target     prot opt source               destination         
KUBE-MARK-MASQ  tcp  --  0.0.0.0/0            0.0.0.0/0            /* default/nginx-svc: */ tcp dpt:30080
KUBE-SVC-R2VK7O5AFVLRAXSH  tcp  --  0.0.0.0/0            0.0.0.0/0            /* default/nginx-svc: */ tcp dpt:30080

Chain KUBE-POSTROUTING (1 references)
target     prot opt source               destination         
MASQUERADE  all  --  0.0.0.0/0            0.0.0.0/0            /* kubernetes service traffic requiring SNAT */ mark match 0x4000/0x4000

Chain KUBE-SEP-2JVQP42V4GXGTRDZ (1 references)
target     prot opt source               destination         
KUBE-MARK-MASQ  all  --  10.244.0.25          0.0.0.0/0            /* kube-system/kube-dns:dns-tcp */
DNAT       tcp  --  0.0.0.0/0            0.0.0.0/0            /* kube-system/kube-dns:dns-tcp */ tcp to:10.244.0.25:53

Chain KUBE-SEP-AZ26OUDW2ONMCF3B (1 references)
target     prot opt source               destination         
KUBE-MARK-MASQ  all  --  10.244.0.24          0.0.0.0/0            /* kube-system/kube-dns:dns */
DNAT       udp  --  0.0.0.0/0            0.0.0.0/0            /* kube-system/kube-dns:dns */ udp to:10.244.0.24:53

Chain KUBE-SEP-KPC3R4X2272VTT4E (1 references)
target     prot opt source               destination         
KUBE-MARK-MASQ  all  --  172.20.0.70          0.0.0.0/0            /* default/kubernetes:https */
DNAT       tcp  --  0.0.0.0/0            0.0.0.0/0            /* default/kubernetes:https */ tcp to:172.20.0.70:6443

Chain KUBE-SEP-NQYSJ3QY2ADXHRG3 (1 references)
target     prot opt source               destination         
KUBE-MARK-MASQ  all  --  10.244.0.25          0.0.0.0/0            /* kube-system/kube-dns:dns */
DNAT       udp  --  0.0.0.0/0            0.0.0.0/0            /* kube-system/kube-dns:dns */ udp to:10.244.0.25:53

Chain KUBE-SEP-WZIMOURZMGKYESDR (1 references)
target     prot opt source               destination         
KUBE-MARK-MASQ  all  --  10.244.1.3           0.0.0.0/0            /* default/nginx-svc: */
DNAT       tcp  --  0.0.0.0/0            0.0.0.0/0            /* default/nginx-svc: */ tcp to:10.244.1.3:80

Chain KUBE-SEP-X5LPZOF2HZFMFFC2 (1 references)
target     prot opt source               destination         
KUBE-MARK-MASQ  all  --  10.244.0.24          0.0.0.0/0            /* kube-system/kube-dns:dns-tcp */
DNAT       tcp  --  0.0.0.0/0            0.0.0.0/0            /* kube-system/kube-dns:dns-tcp */ tcp to:10.244.0.24:53

Chain KUBE-SERVICES (2 references)
target     prot opt source               destination         
KUBE-MARK-MASQ  tcp  -- !10.244.0.0/16        10.96.0.1            /* default/kubernetes:https cluster IP */ tcp dpt:443
KUBE-SVC-NPX46M4PTMTKRN6Y  tcp  --  0.0.0.0/0            10.96.0.1            /* default/kubernetes:https cluster IP */ tcp dpt:443
KUBE-MARK-MASQ  udp  -- !10.244.0.0/16        10.96.0.10           /* kube-system/kube-dns:dns cluster IP */ udp dpt:53
KUBE-SVC-TCOU7JCQXEZGVUNU  udp  --  0.0.0.0/0            10.96.0.10           /* kube-system/kube-dns:dns cluster IP */ udp dpt:53
KUBE-MARK-MASQ  tcp  -- !10.244.0.0/16        10.96.0.10           /* kube-system/kube-dns:dns-tcp cluster IP */ tcp dpt:53
KUBE-SVC-ERIFXISQEP7F7OF4  tcp  --  0.0.0.0/0            10.96.0.10           /* kube-system/kube-dns:dns-tcp cluster IP */ tcp dpt:53
KUBE-MARK-MASQ  tcp  -- !10.244.0.0/16        10.108.205.52        /* default/nginx-svc: cluster IP */ tcp dpt:80
KUBE-SVC-R2VK7O5AFVLRAXSH  tcp  --  0.0.0.0/0            10.108.205.52        /* default/nginx-svc: cluster IP */ tcp dpt:80
KUBE-NODEPORTS  all  --  0.0.0.0/0            0.0.0.0/0            /* kubernetes service nodeports; NOTE: this must be the last rule in this chain */ ADDRTYPE match dst-type LOCAL

Chain KUBE-SVC-ERIFXISQEP7F7OF4 (1 references)
target     prot opt source               destination         
KUBE-SEP-X5LPZOF2HZFMFFC2  all  --  0.0.0.0/0            0.0.0.0/0            /* kube-system/kube-dns:dns-tcp */ statistic mode random probability 0.50000000000
KUBE-SEP-2JVQP42V4GXGTRDZ  all  --  0.0.0.0/0            0.0.0.0/0            /* kube-system/kube-dns:dns-tcp */

Chain KUBE-SVC-NPX46M4PTMTKRN6Y (1 references)
target     prot opt source               destination         
KUBE-SEP-KPC3R4X2272VTT4E  all  --  0.0.0.0/0            0.0.0.0/0            /* default/kubernetes:https */

Chain KUBE-SVC-R2VK7O5AFVLRAXSH (2 references)
target     prot opt source               destination         
KUBE-SEP-WZIMOURZMGKYESDR  all  --  0.0.0.0/0            0.0.0.0/0            /* default/nginx-svc: */

Chain KUBE-SVC-TCOU7JCQXEZGVUNU (1 references)
target     prot opt source               destination         
KUBE-SEP-AZ26OUDW2ONMCF3B  all  --  0.0.0.0/0            0.0.0.0/0            /* kube-system/kube-dns:dns */ statistic mode random probability 0.50000000000
KUBE-SEP-NQYSJ3QY2ADXHRG3  all  --  0.0.0.0/0            0.0.0.0/0            /* kube-system/kube-dns:dns */
