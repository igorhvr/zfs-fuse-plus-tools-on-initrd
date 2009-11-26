
programs= ("bin/umount", "bin/mount", "bin/busybox", "sbin/cryptsetup",  "sbin/strace", "sbin/dmsetup",  
    "bin/fuser", "sbin/zstreamdump", "bin/ldd", "sbin/ldconfig",  
    "sbin/insmod", "sbin/modprobe", "bin/lsmod", "sbin/rmmod", 
    "bin/rsync","sbin/fdisk","sbin/cfdisk"  , 
    "sbin/pivot_root", 
    "bin/btrfs", "bin/btrfsck", "bin/btrfsctl", "bin/btrfs-debug-tree", "bin/btrfs-image", "bin/btrfs-map-logical", "bin/btrfs-show", "bin/btrfstune", "bin/btrfs-vol", "bin/mkfs.btrfs", 
          
    "sbin/zdb", "sbin/zfs", "sbin/zfs-fuse", "sbin/zinject", "sbin/zpios", "sbin/zpool", "sbin/zstreamdump", "sbin/ztest",


    "/sbin/fsck.ext2", "/sbin/fsck.ext3", "/sbin/fsck.ext4", "/sbin/fsck.ext4dev", "/sbin/mkfs.ext2", "/sbin/mkfs.ext3", "/sbin/mkfs.ext4"
)
extralibs=(

"/lib/libnss_compat-2.11.2.so", "/lib/libnss_compat.so.2", "/lib/libnss_dns-2.11.2.so", "/lib/libnss_dns.so.2", "/lib/libnss_files-2.11.2.so", "/lib/libnss_files.so.2", "/lib/libnss_hesiod-2.11.2.so", "/lib/libnss_hesiod.so.2", "/lib/libnss_mdns4_minimal.so.2", "/lib/libnss_mdns4.so.2", "/lib/libnss_mdns6_minimal.so.2", "/lib/libnss_mdns6.so.2", "/lib/libnss_mdns_minimal.so.2", "/lib/libnss_mdns.so.2", "/lib/libnss_nis-2.11.2.so", "/lib/libnss_nisplus-2.11.2.so", "/lib/libnss_nisplus.so.2", "/lib/libnss_nis.so.2", "/lib64/libnss_compat-2.11.2.so", "/lib64/libnss_compat.so.2", "/lib64/libnss_dns-2.11.2.so", "/lib64/libnss_dns.so.2", "/lib64/libnss_files-2.11.2.so", "/lib64/libnss_files.so.2", "/lib64/libnss_hesiod-2.11.2.so", "/lib64/libnss_hesiod.so.2", "/lib64/libnss_nis-2.11.2.so", "/lib64/libnss_nisplus-2.11.2.so", "/lib64/libnss_nisplus.so.2", "/lib64/libnss_nis.so.2"
  )



#$ ls bin/*btrfs*|perl -n -e 'chomp ($_); print "\"".$_."\", "'
