<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jenkins CI/CD Pipeline – EKS Deployment</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            padding: 40px;
        }

        h1 {
            text-align: center;
            margin-bottom: 40px;
        }

        .pipeline {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
        }

        .stage {
            background: white;
            border-radius: 10px;
            width: 220px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        .stage h3 {
            margin-top: 0;
            color: #0b5ed7;
        }

        .arrow {
            font-size: 30px;
            color: #555;
        }

        footer {
            margin-top: 50px;
            text-align: center;
            color: #777;
            font-size: 14px;
        }
    </style>
</head>
<body>

<h1>🚀 Jenkins CI/CD Pipeline – AWS EKS</h1>

<div class="pipeline">

    <div class="stage">
        <h3>Checkout Code</h3>
        <p>GitHub Repository</p>
        <p><strong>Branch:</strong> main</p>
    </div>

    <div class="arrow">➡️</div>

    <div class="stage">
        <h3>Build Image</h3>
        <p>Docker Build</p>
        <p>Tag: BUILD_NUMBER</p>
    </div>

    <div class="arrow">➡️</div>

    <div class="stage">
        <h3>Push to ECR</h3>
        <p>AWS ECR</p>
        <p>Latest & Versioned</p>
    </div>

    <div class="arrow">➡️</div>

    <div class="stage">
        <h3>Deploy to EKS</h3>
        <p>Kubernetes</p>
        <p>kubectl apply</p>
    </div>

</div>

<footer>
    Jenkins Declarative Pipeline | AWS ECR & EKS
</footer>

</body>
</html>
