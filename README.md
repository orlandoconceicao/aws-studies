# ☁️ AWS CLOUD STUDIES — GUIA COMPLETO

Repositório com estudos práticos, organizados e estruturados dos principais serviços da AWS.

Projeto focado em arquitetura profissional, boas práticas, segurança, escalabilidade e mentalidade de arquiteto cloud.

---

# 📂 ESTRUTURA DO PROJETO

```
aws-cloud-studies/
│
├── aws-dynamodb/
├── aws-ec2/
├── aws-ec2-g4/
├── aws-iam/
├── aws-lambda/
├── aws-rds/
├── aws-s3/
├── aws-s3-glacier/
├── aws-shield/
├── aws-sns/
├── aws-sqs/
├── aws-step-functions/
├── aws-vpc/
│
├── .venv/
├── __pycache__/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

Cada pasta representa um serviço estudado com aplicação prática e visão arquitetural.

---

# 🚀 SERVIÇOS ESTUDADOS

## 🖥️ Computação

- **aws-ec2** → Servidores virtuais escaláveis (IaaS)
- **aws-ec2-g4** → EC2 com GPU para alto desempenho
- **aws-lambda** → Computação serverless baseada em eventos

---

## 🗄️ Banco de Dados

- **aws-rds** → Banco relacional gerenciado (PostgreSQL, MySQL)
- **aws-dynamodb** → Banco NoSQL serverless altamente escalável

---

## 📦 Armazenamento

- **aws-s3** → Armazenamento de objetos altamente durável
- **aws-s3-glacier** → Armazenamento de arquivamento de baixo custo

---

## 📩 Mensageria e Orquestração

- **aws-sqs** → Fila de mensagens (processamento assíncrono)
- **aws-sns** → Sistema Pub/Sub e notificações
- **aws-step-functions** → Orquestração de workflows distribuídos

---

## 🔐 Segurança e Rede

- **aws-iam** → Controle de acesso e permissões
- **aws-vpc** → Rede privada virtual isolada
- **aws-shield** → Proteção contra ataques DDoS

---

# 🎯 OBJETIVO DO REPOSITÓRIO

- Consolidar conhecimento profundo em AWS
- Simular arquiteturas reais de produção
- Aplicar boas práticas de segurança
- Estruturar projetos com padrão profissional
- Evoluir mentalidade de desenvolvedor para arquiteto cloud

---

# 🏗️ ARQUITETURA DE REFERÊNCIA

```
Internet
   ↓
Route 53
   ↓
CloudFront
   ↓
Shield + WAF
   ↓
Load Balancer
   ↓
EC2 / Lambda
   ↓
RDS / DynamoDB
   ↓
SQS / SNS
   ↓
Step Functions
```

Essa arquitetura representa um modelo escalável, seguro e desacoplado.

---

# 🔐 BOAS PRÁTICAS APLICADAS

- Uso de IAM Role ao invés de Access Key
- Princípio do menor privilégio (Least Privilege)
- Separação entre ambientes (dev / prod)
- Arquitetura desacoplada
- Proteção em múltiplas camadas
- Banco de dados em subnet privada
- Monitoramento com CloudWatch
- Uso de serviços gerenciados sempre que possível

---

# 🧠 CONCEITOS CONSOLIDADOS

✔ Infraestrutura como Serviço (IaaS)  
✔ Computação Serverless  
✔ Arquitetura Event-Driven  
✔ Processamento Assíncrono  
✔ Segurança em Camadas  
✔ Alta Disponibilidade  
✔ Escalabilidade Horizontal  
✔ Desacoplamento de Serviços  
✔ Resiliência e tolerância a falhas  

---

# 📚 TECNOLOGIAS UTILIZADAS

- Python
- Boto3
- AWS CLI
- IAM Roles
- Terraform (infraestrutura opcional)
- CloudWatch

---

# 🎯 VISÃO PROFISSIONAL

Este repositório simula cenários reais de mercado, como:

- Backend escalável com EC2 e Load Balancer
- APIs serverless com Lambda
- Banco relacional com RDS
- Banco NoSQL com DynamoDB
- Processamento assíncrono com SQS
- Comunicação entre serviços com SNS
- Orquestração de fluxos com Step Functions
- Proteção DDoS com Shield
- Rede isolada com VPC

---

# ⭐ CONCLUSÃO

Este repositório representa a construção de uma stack completa AWS, abrangendo:

Computação  
Banco de Dados  
Mensageria  
Segurança  
Rede  
Proteção DDoS  

Base sólida para atuação como:

- Backend Developer Cloud  
- DevOps Engineer  
- Cloud Engineer  
- Arquiteto de Soluções AWS  

---

# 👨‍💻 Autor

**Orlando Conceição**  
Cloud & Backend Developer  

📧 Contato: orlandoconceicao94@gmail.com  

---
