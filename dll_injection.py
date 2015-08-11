import ctypes

PAGE_READWRITE=0x04
PROCESS_ALL_ACCESS=(0x000F0000 | 0x0010000 | 0xFFF)
VIRTUAL_MEM= (0x1000 | 0x2000)

                    

def DLLinject(DLLPath,PID):
    kernel32=ctypes.windll.kernel32
    dll_path=DLLPath
    len_dll=len(dll_path)
    HProcess=kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, int(pid))
    arg_addr=kernel32.VirtualAllocEx(HProcess,0,len_dll,VIRTUAL_MEM,PAGE_READWRITE)
    wrttn=ctypes.c_int(0)
    kernel32.WriteProcessMemory(HProcess,arg_addr,dll_path,len_dll,
    ctypes.byref(wrttn))
    HK32=kernel32.GetModuleHandleA("kernel32.dll")
    HLL=kernel32.GetProcAddress(HK32,"LoadLibraryA")
    thr_id=ctypes.c_i=ulong(0)
    kernel.CreateRemoteThread(HProcess,None,0,HLL,arg_addr,0,ctypes.byref(thr_id))
    return thr_id
