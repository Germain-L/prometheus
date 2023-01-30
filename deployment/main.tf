resource "azurerm_resource_group" "rg" {
  name     = "kube-prometheus-stack"
  location = "westeurope"
}

resource "azurerm_container_registry" "acr" {
  name                = "kubeprometheusacr"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
}

resource "azurerm_container_registry_task" "task" {
  count                 = length(var.images)
  name                  = "build-task-${var.images[count.index]}"
  container_registry_id = azurerm_container_registry.acr.id
  platform {
    os = "Linux"
  }
  docker_step {
    dockerfile_path      = "Dockerfile"
    context_path         = "https://github.com/Germain-L/prometheus.git#kubernetes:${var.images[count.index]}"
    context_access_token = var.GITHUB_ACCESS_TOKEN
    image_names          = ["${var.images[count.index]}:latest"]
  }
}

resource "azurerm_container_registry_task_schedule_run_now" "build" {
  count                      = length(var.images)
  container_registry_task_id = azurerm_container_registry_task.task[count.index].id
}

