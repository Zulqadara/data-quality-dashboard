provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "dataset_bucket" {
  bucket = var.bucket_name
}

resource "aws_ecs_cluster" "dq_cluster" {
  name = "dq-cluster"
}
