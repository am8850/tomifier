define util_confirm_code
$(eval confirm := $(shell read -p "⚠ Are you sure? [y/n] > " -r; echo $$REPLY))
$(if $(filter y Y,$(confirm)),1)
endef
#NOTE: We must call this one to remove \n or any other spaces
util_confirm_ask = $(strip $(util_confirm_code))

.PHONY: default
default:
	@echo "Please specify a target to make"

.PHONY: build
build:
	sh build.sh

.PHONY: publish
publish:
	twine upload dist/*

VERSION=0.0.4
.PHONY: tag
tag:
	git tag -a v$(VERSION) -m "v$(VERSION)"
	git push origin v$(VERSION)
