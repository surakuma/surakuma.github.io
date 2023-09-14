#include <bits/stdc++.h>
using namespace std;

#define N 500
#define ITER 10
bool sameArrays(double* calc, double * ref, int n)
{
    for(int i=0; i<n; i++)
    {
        if(calc[i] != ref[i])
            return false;
    }
    return true;
}
int main()
{
    double *A = new double[N*N];
    double *B = new double[N*N];
    double *C = new double[N*N];
    double *Cref = new double[N*N];

    //Assign values in arrays A and B
    for(int i=0; i<N; i++)
    {
        for(int j=0; j<N; j++)
        {
            A[i*N+j] = (i+j*j)%7;
            B[i*N+j] = (i*i+j*j*j)%7;
            C[i*N+j] = 0;
            Cref[i*N+j] = 0;
        }
    }

    for(int i=0; i<N; i++)
    {
        for(int j=0; j<N; j++)
        {
            for(int k=0; k< N; k++)
                Cref[i*N+j] += A[i*N+k]*B[k*N+j];
        }
    }

    clock_t start, end;
    double total_time_taken;

    //(i,j,k) -- permutation
    total_time_taken= 0;
    for(int iter=0; iter <ITER; iter++)
    {
        for(int i=0; i<N*N; i++)
            C[i] = 0;


        start = clock();
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {
                for(int k=0; k< N; k++)
                    C[i*N+j] += A[i*N+k]*B[k*N+j];
            }
        }
        end = clock();
        

        total_time_taken += double(end - start) / double(CLOCKS_PER_SEC);

        if(!sameArrays(C, Cref, N*N))
        {
            cout << "(i,j,k) permutation not producing correct output in " << iter << "iterations , exiting..." << endl;
            exit(0);
        }
        if(iter == ITER -1)
            cout << "(i,j,k) permutation timing : "<< fixed << total_time_taken/ITER << setprecision(5) << " sec" <<endl;
    }

    //(i,k,j) -- permutation
    total_time_taken= 0;
    for(int iter=0; iter <ITER; iter++)
    {
        for(int i=0; i<N*N; i++)
            C[i] = 0;
        

        start = clock();
        for(int i=0; i<N; i++)
        {
            for(int k=0; k< N; k++)
            {
                for(int j=0; j<N; j++)
                    C[i*N+j] += A[i*N+k]*B[k*N+j];
            }
        }
        end = clock();
        

        total_time_taken += double(end - start) / double(CLOCKS_PER_SEC);

        if(!sameArrays(C, Cref, N*N))
        {
            cout << "(i,k,j) permutation not producing correct output in " << iter << "iterations , exiting..." << endl;
            exit(0);
        }
        if(iter == ITER -1)
            cout << "(i,k,j) permutation timing : "<< fixed << total_time_taken/ITER << setprecision(5) << " sec" <<endl;
    }


    //(j,i,k) -- permutation
    total_time_taken= 0;
    for(int iter=0; iter <ITER; iter++)
    {
        for(int i=0; i<N*N; i++)
            C[i] = 0;
        

        start = clock();
        for(int j=0; j<N; j++)
        {
            for(int i=0; i<N; i++)
            {
                for(int k=0; k< N; k++)
                    C[i*N+j] += A[i*N+k]*B[k*N+j];
            }
        }
        end = clock();
        

        total_time_taken += double(end - start) / double(CLOCKS_PER_SEC);

        if(!sameArrays(C, Cref, N*N))
        {
            cout << "(j,i,k) permutation not producing correct output in " << iter << "iterations , exiting..." << endl;
            exit(0);
        }
        if(iter == ITER -1)
            cout << "(j,i,k) permutation timing : "<< fixed << total_time_taken/ITER << setprecision(5) << " sec" <<endl;
    }


    //(j,k,i) -- permutation
    total_time_taken= 0;
    for(int iter=0; iter <ITER; iter++)
    {
        for(int i=0; i<N*N; i++)
            C[i] = 0;
        

        start = clock();
        for(int j=0; j<N; j++)
        {
            for(int k=0; k< N; k++)
            {
                for(int i=0; i<N; i++)
                    C[i*N+j] += A[i*N+k]*B[k*N+j];
            }
        }
        end = clock();
        

        total_time_taken += double(end - start) / double(CLOCKS_PER_SEC);

        if(!sameArrays(C, Cref, N*N))
        {
            cout << "(j,k,i) permutation not producing correct output in " << iter << "iterations , exiting..." << endl;
            exit(0);
        }
        if(iter == ITER -1)
            cout << "(j,k,i) permutation timing : "<< fixed << total_time_taken/ITER << setprecision(5) << " sec" <<endl;
    }


    //(k,i,j) -- permutation
    total_time_taken= 0;
    for(int iter=0; iter <ITER; iter++)
    {
        for(int i=0; i<N*N; i++)
            C[i] = 0;
        

        start = clock();
        for(int k=0; k< N; k++)
        {
            for(int i=0; i<N; i++)
            {
                for(int j=0; j<N; j++)
                    C[i*N+j] += A[i*N+k]*B[k*N+j];
            }
        }
        end = clock();
        

        total_time_taken += double(end - start) / double(CLOCKS_PER_SEC);

        if(!sameArrays(C, Cref, N*N))
        {
            cout << "(k,i,j) permutation not producing correct output in " << iter << "iterations , exiting..." << endl;
            exit(0);
        }
        if(iter == ITER -1)
            cout << "(k,i,j) permutation timing : "<< fixed << total_time_taken/ITER << setprecision(5) << " sec" <<endl;
    }


    //(k,j,i) -- permutation
    total_time_taken= 0;
    for(int iter=0; iter <ITER; iter++)
    {
        for(int i=0; i<N*N; i++)
            C[i] = 0;
        

        start = clock();
        for(int k=0; k< N; k++)
        {
            for(int j=0; j<N; j++)
            {
                for(int i=0; i<N; i++)
                    C[i*N+j] += A[i*N+k]*B[k*N+j];
            }
        }
        end = clock();
        

        total_time_taken += double(end - start) / double(CLOCKS_PER_SEC);

        if(!sameArrays(C, Cref, N*N))
        {
            cout << "(k,j,i) permutation not producing correct output in " << iter << "iterations , exiting..." << endl;
            exit(0);
        }
        if(iter == ITER -1)
            cout << "(k,j,i) permutation timing : "<< fixed << total_time_taken/ITER << setprecision(5) << " sec" <<endl;
    }


    delete[] Cref;
    delete[] C;
    delete[] B;
    delete[] A;
}
