provider "google" {
  project = "projeto-aurora-id"
  region  = "us-central1"
}

resource "google_compute_instance" "app_server" {
  name         = "lord-eclipse-instance"
  machine_type = "f1-micro"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {
    }
  }
}
