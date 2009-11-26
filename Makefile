.PHONY: initrd.gz


all:
	./update-programs.py
	./collect-libs.py

initrd.gz: 
	./gen-image-from-to source initrd.gz


clean:
	./clean-libraries
	./clean-programs.py
	rm initrd.gz

