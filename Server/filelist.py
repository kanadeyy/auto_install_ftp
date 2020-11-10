import errno, os, winreg

def filelist1():
    proc_Arch = os.environ['PROCESSOR_ARCHITECTURE'].lower()
    proc_Arch64 = os.environ['PROCESSOR_ARCHITEW6432'].lower()
    programbuffer = []

    if proc_Arch == 'x86' and not proc_Arch64:
        Arch_keys = {0}
    elif proc_Arch == 'x86' or proc_Arch == 'AMD64':
        Arch_keys = {winreg.KEY_WOW64_32KEY, winreg.KEY_WOW64_64KEY}
    else:
        raise Exception("Unhandled Arch: %s" % proc_Arch)

    for Arch_key in Arch_keys:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | Arch_key)
        for i in range(0, winreg.QueryInfoKey(key)[0]):
            skey_name = winreg.EnumKey(key, i)
            skey = winreg.OpenKey(key, skey_name)
            try:
                a = str(winreg.QueryValueEx(skey, 'InstallLocation')[0])
                b = str(winreg.QueryValueEx(skey, 'DisplayName')[0])
                if a != "" and "NVIDIA" not in b:
                    programbuffer.append([b,a])
            except OSError as e:
                if e.errno == errno.ENOENT:

                    pass
            finally:
                skey.Close()

    return programbuffer

def filelist2():
    proc_Arch = os.environ['PROCESSOR_ARCHITECTURE'].lower()
    proc_Arch64 = os.environ['PROCESSOR_ARCHITEW6432'].lower()
    programbuffer = []

    if proc_Arch == 'x86' and not proc_Arch64:
        Arch_keys = {0}
    elif proc_Arch == 'x86' or proc_Arch == 'AMD64':
        Arch_keys = {winreg.KEY_WOW64_32KEY, winreg.KEY_WOW64_64KEY}
    else:
        raise Exception("Unhandled Arch: %s" % proc_Arch)

    for Arch_key in Arch_keys:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | Arch_key)
        for i in range(0, winreg.QueryInfoKey(key)[0]):
            skey_name = winreg.EnumKey(key, i)
            skey = winreg.OpenKey(key, skey_name)
            try:
                a = str(winreg.QueryValueEx(skey, 'InstallLocation')[0])
                b = str(winreg.QueryValueEx(skey, 'DisplayName')[0])
                if a != "" and "NVIDIA" not in b:
                    programbuffer.append([b,a])
            except OSError as e:
                if e.errno == errno.ENOENT:

                    pass
            finally:
                skey.Close()

    return programbuffer

def duplecheck():
    temp_buffer1 = filelist1()
    temp_buffer2 = filelist2()

    programlist = []
    programlocation = []

    temp_buffer = temp_buffer1+temp_buffer2

    final_buffer = []

    for i in range(0,len(temp_buffer)):
        if temp_buffer[i] not in final_buffer:
            final_buffer.append(temp_buffer[i])

    for i in range(0,len(final_buffer)):
        programlist.append(final_buffer[i][0])
        programlocation.append(final_buffer[i][1])

    return final_buffer, programlist, programlocation
