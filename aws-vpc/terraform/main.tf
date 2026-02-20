provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "vpc_principal" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "vpc-producao"
  }
}

resource "aws_subnet" "subnet_publica" {
  vpc_id                  = aws_vpc.vpc_principal.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true

  tags = {
    Name = "subnet-publica"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc_principal.id

  tags = {
    Name = "internet-gateway"
  }
}
