.PHONY: initrd.gz


all:
	./update-programs.py
	./collect-libs.py
	chroot source ldconfig


initrd.gz: 
	./check_debian
	./gen-image-from-to source initrd.gz


clean:
	./clean-libraries
	./clean-programs.py
	rm initrd.gz

install: initrd.gz
#	mount /boot
	cp -v initrd.gz /boot/boot/
#	umount /boot
