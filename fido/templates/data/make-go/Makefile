TARGET=#PROJECT_NAME#

all: deps build

deps: godep golint gomegacheck
	@dep ensure

build:
	@go build -o $(TARGET) .

clean:
	@rm -rf $(TARGET)
	@rm -rf build

install:
	@cp $(TARGET) /usr/local/bin/

godep:
	@go get -u github.com/golang/dep/...

golint:
	@go get github.com/golang/lint/golint

gomegacheck:
	@go get honnef.co/go/tools/cmd/megacheck
