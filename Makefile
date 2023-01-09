NAME= $(shell grep Name: *.spec | sed 's/^[^:]*:[^a-zA-Z]*//' )
VERSION= $(shell grep Version: *.spec | sed 's/^[^:]*:[^0-9]*//' )
RELEASE= $(shell grep Release: *.spec |cut -d"%" -f1 |sed 's/^[^:]*:[^0-9]*//')
build=$(shell pwd)/build
DATE=$(shell date "+%a, %d %b %Y %T %z")
dist=$(shell rpm --eval '%dist' | sed 's/%dist/.el5/')

default:
	@echo "Nothing to do"

install:
	@echo installing ...
	@install -d ${prefix}/etc/ldap/schema
	@install --mode=0644 etc/ldap/schema/*.schema ${prefix}/etc/ldap/schema
	@mkdir -p $(prefix)/usr/share/doc/glue-schema/
	@install -m 0644 README.md $(prefix)/usr/share/doc/glue-schema/
	@install -m 0644 AUTHORS.md $(prefix)/usr/share/doc/glue-schema/
	@install -m 0644 COPYRIGHT $(prefix)/usr/share/doc/glue-schema/
	@install -m 0644 LICENSE.txt $(prefix)/usr/share/doc/glue-schema/

dist:
	@mkdir -p  $(build)/$(NAME)-$(VERSION)/
	rsync -HaS --exclude ".git" --exclude "$(build)" * $(build)/$(NAME)-$(VERSION)/
	cd $(build); tar --gzip -cf $(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)/; cd -

sources: dist
	cp $(build)/$(NAME)-$(VERSION).tar.gz .

deb: dist
	cd $(build)/$(NAME)-$(VERSION); dpkg-buildpackage -us -uc; cd -

prepare: dist
	@mkdir -p  $(build)/RPMS/noarch
	@mkdir -p  $(build)/SRPMS/
	@mkdir -p  $(build)/SPECS/
	@mkdir -p  $(build)/SOURCES/
	@mkdir -p  $(build)/BUILD/
	cp $(build)/$(NAME)-$(VERSION).tar.gz $(build)/SOURCES
	cp $(NAME).spec $(build)/SPECS

srpm: prepare
	rpmbuild -bs --define="dist ${dist}" --define='_topdir ${build}' $(build)/SPECS/$(NAME).spec

rpm: srpm
	rpmbuild --rebuild  --define='_topdir ${build}' --define="dist ${dist}" $(build)/SRPMS/$(NAME)-$(VERSION)-$(RELEASE)${dist}.src.rpm

clean:
	rm -f *~ $(NAME)-$(VERSION).tar.gz
	rm -rf $(build)

.PHONY: dist srpm rpm sources clean
